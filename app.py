import os
import streamlit as st
import tempfile
from typing import List, Dict

# Import existing components
from agents.paper_search import search_semantic_scholar
from agents.topic_and_summary import classify_topic, summarize_text
from agents.audio import text_to_audio
from utils.pdf_loader import load_pdf
from utils.url_loader import load_pdf_from_url

# Set page configuration
st.set_page_config(
    page_title="Research Paper Analysis System",
    page_icon="",
    layout="wide"
)

# Create output directories
os.makedirs("outputs", exist_ok=True)
os.makedirs("outputs/summaries", exist_ok=True)
os.makedirs("outputs/audio", exist_ok=True)

# Initialize session state variables
if "papers" not in st.session_state:
    st.session_state.papers = []
if "paper_contents" not in st.session_state:
    st.session_state.paper_contents = {}
if "processed_papers" not in st.session_state:
    st.session_state.processed_papers = {}

# Function to process a paper
def process_paper(title: str, content: str, topics: List[str]):
    # Classify the paper
    paper_topic = classify_topic(content[:5000], topics)  # Use first 5000 chars for classification
    
    # Generate summary
    summary = summarize_text(content)
    
    # Save summary to file
    summary_path = f"outputs/summaries/{title.replace(' ', '_')}.txt"
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(summary)
    
    # Generate audio
    audio_path = f"{title.replace(' ', '_')}.mp3"
    text_to_audio(summary, audio_path)
    
    return {
        "title": title,
        "topic": paper_topic,
        "summary": summary,
        "summary_path": summary_path,
        "audio_path": f"outputs/{audio_path}"
    }

# Main app layout
st.title(" Multi-Agent Research Paper Processor")
st.write("Find, analyze, and summarize research papers with audio podcast generation")

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    
    # Topic configuration
    st.subheader("Topics for Classification")
    default_topics = ["Artificial Intelligence", "Medical Imaging", "Computer Vision", "Data Science"]
    topics_text = st.text_area("Enter topics (one per line)", "\n".join(default_topics))
    topics = [t.strip() for t in topics_text.split("\n") if t.strip()]

# Create tabs for different functionality
tab1, tab2, tab3, tab4 = st.tabs(["Paper Search", "PDF Upload", "URL Input", "Results"])

# Tab 1: Paper Search
with tab1:
    st.header(" Search for Research Papers")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        search_query = st.text_input("Enter search query")
    
    with col2:
        limit = st.number_input("Result limit", min_value=1, max_value=30, value=3)
    
    if st.button("Search") and search_query:
        with st.spinner("Searching for papers..."):
            search_results = search_semantic_scholar(search_query, limit)
            
            if search_results:
                st.success(f"Found {len(search_results)} papers")
                st.session_state.papers = search_results
                
                # Display search results
                for i, paper in enumerate(search_results):
                    with st.expander(f"{i+1}. {paper['title']}"):
                        st.write(f"**Title:** {paper['title']}")
                        st.write(f"**Semantic Scholar:** [Link]({paper.get('semanticscholar_url', '#')})")
                        
                        pdf_url = paper.get('pdf_url')
                        if pdf_url:
                            st.write(f"**PDF URL:** [Link]({pdf_url})")
                            
                            if st.button(f"Process Paper #{i+1}", key=f"process_search_{i}"):
                                with st.spinner(f"Processing paper: {paper['title']}..."):
                                    try:
                                        # Download and process the paper
                                        content = load_pdf_from_url(pdf_url)
                                        st.session_state.paper_contents[paper['title']] = content
                                        
                                        # Process the paper
                                        result = process_paper(paper['title'], content, topics)
                                        st.session_state.processed_papers[paper['title']] = result
                                        
                                        st.success(f"Successfully processed paper: {paper['title']}")
                                    except Exception as e:
                                        st.error(f"Error processing paper: {str(e)}")
                        else:
                            st.warning("No PDF URL available for this paper")
            else:
                st.warning("No papers found. Try a different search query.")

# Tab 2: PDF Upload
with tab2:
    st.header(" Upload PDF File")
    
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Get filename without extension
        file_name = os.path.splitext(uploaded_file.name)[0]
        
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.getvalue())
            temp_path = temp_file.name
        
        st.success(f"File uploaded: {uploaded_file.name}")
        
        if st.button("Process PDF"):
            with st.spinner("Processing PDF..."):
                try:
                    # Load and process the PDF
                    content = load_pdf(temp_path)
                    st.session_state.paper_contents[file_name] = content
                    
                    # Add to papers list
                    st.session_state.papers.append({
                        "title": file_name,
                        "source": "file",
                        "file_path": temp_path
                    })
                    
                    # Process the paper
                    result = process_paper(file_name, content, topics)
                    st.session_state.processed_papers[file_name] = result
                    
                    st.success(f"Successfully processed PDF: {file_name}")
                except Exception as e:
                    st.error(f"Error processing PDF: {str(e)}")
                finally:
                    # Clean up the temporary file
                    try:
                        os.unlink(temp_path)
                    except:
                        pass

# Tab 3: URL Input
with tab3:
    st.header(" Process Paper from URL")
    
    url = st.text_input("Enter URL to PDF file")
    custom_title = st.text_input("Custom title (optional)")
    
    if st.button("Process URL") and url:
        with st.spinner("Processing paper from URL..."):
            try:
                # Extract title from URL if custom title not provided
                title = custom_title if custom_title else url.split("/")[-1].replace('.pdf', '')
                
                # Download and process the PDF
                content = load_pdf_from_url(url)
                st.session_state.paper_contents[title] = content
                
                # Add to papers list
                st.session_state.papers.append({
                    "title": title,
                    "source": "url",
                    "url": url
                })
                
                # Process the paper
                result = process_paper(title, content, topics)
                st.session_state.processed_papers[title] = result
                
                st.success(f"Successfully processed paper from URL: {title}")
            except Exception as e:
                st.error(f"Error processing paper from URL: {str(e)}")

# Tab 4: Results
with tab4:
    st.header(" Processed Papers")
    
    if not st.session_state.processed_papers:
        st.info("No papers have been processed yet. Process a paper to see results here.")
    else:
        # Display processed papers
        for title, paper in st.session_state.processed_papers.items():
            with st.expander(f" {title}"):
                st.write(f"**Topic Classification**: {paper['topic']}")
                
                st.subheader("Summary")
                st.write(paper['summary'])
                
                # Audio player
                st.subheader("Audio Summary")
                if os.path.exists(paper['audio_path']):
                    st.audio(paper['audio_path'])
                else:
                    st.warning("Audio file not found")
                
                # Download buttons
                col1, col2 = st.columns(2)
                with col1:
                    if os.path.exists(paper['summary_path']):
                        with open(paper['summary_path'], 'r', encoding='utf-8') as f:
                            summary_text = f.read()
                        st.download_button(
                            label="Download Summary",
                            data=summary_text,
                            file_name=f"{title.replace(' ', '_')}_summary.txt",
                            mime="text/plain"
                        )
                
                with col2:
                    if os.path.exists(paper['audio_path']):
                        with open(paper['audio_path'], 'rb') as f:
                            audio_data = f.read()
                        st.download_button(
                            label="Download Audio",
                            data=audio_data,
                            file_name=f"{title.replace(' ', '_')}_audio.mp3",
                            mime="audio/mp3"
                        )

# Footer
st.markdown("---")
st.caption("Research Paper Analysis System - VahanAI")