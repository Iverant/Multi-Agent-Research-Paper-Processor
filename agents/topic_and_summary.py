from config import API_KEY_openai
from config import API_KEY_langsmith
import os

os.environ["OPENAI_API_KEY"] = API_KEY_openai
os.environ["LANGCHAIN_API_KEY"] = API_KEY_langsmith
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_ENDPOINT'] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "VahanAI"

from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def classify_topic(text: str, topics: list):
    
    prompt = PromptTemplate(
        input_variables = ["text", "topics"],
                template="""You are an academic topic classifier. 
                    Given a research paper abstract (or introduction), classify it into only one of the following user-defined topics: {topics}.

                    Text:
                    {text}

                    Return a single topic from this list."""
    )
    
    llm = ChatOpenAI(temperature = 0.7)
    chain = LLMChain(llm= llm, prompt = prompt)
    
    return chain.run({"text": text, "topics": ",".join(topics)})



def summarize_text(text: str):
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 3000, chunk_overlap = 200)
    
    chunks = text_splitter.split_text(text)
    print(f"Length of chunks: {len(chunks)}")
    
    
    docs = [Document(page_content=chunk) for chunk in chunks]
    
    llm = ChatOpenAI(temperature = 0.7)
    
    
    prompt_template = f"""Summarize the following research paper content in English.
            Provide a structured summary with bullet points under the following headings:
            - Objective
            - Methods
            - Results
            - Limitations
            - Future Work
    
            Text:
            {{text}}
    
            Summary:
            """
            
    prompt = PromptTemplate.from_template(prompt_template)

    refine_template = f"""
        We have an existing summary: {{existing_answer}}

        Refine and improve the summary using the new context below (only if necessary).

        New Context:
        {{text}}

        The final summary in English should follow this structure:
        - Objective
        - Methods
        - Results
        - Limitations
        - Future Work

        If no update is needed, return the existing summary.
        """
    refine_prompt = PromptTemplate.from_template(refine_template)

    summarize_chain = load_summarize_chain(
        llm=llm,
        chain_type="refine",
        question_prompt=prompt,
        refine_prompt=refine_prompt,
        input_key="input_documents",
        output_key="output_text",
        return_intermediate_steps=False,
    )

    result = summarize_chain({"input_documents": docs}, return_only_outputs=True)
    return result["output_text"]
    
    
