from langchain_community.document_loaders import PyPDFLoader # type: ignore

def load_pdf(file_path: str):

    loader = PyPDFLoader(file_path)
    pages = loader.load()
    
    print("success")
    # return [page.page_content for page in pages]
    
    return "\n".join(page.page_content for page in pages)


if __name__ == "__main__":
    file_path = "2305.09011v6.pdf"
    content = load_pdf(file_path)
    # for page in content:
    #     print(page[:500])
    
    print(content)