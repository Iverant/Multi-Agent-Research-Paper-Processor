import requests
from io import BytesIO
from PyPDF2 import PdfReader

def load_pdf_from_url(pdf_url: str):

    # pdf_url = "https://arxiv.org/pdf/2305.09011"

    response = requests.get(pdf_url)
    pdf_in_memory = BytesIO(response.content)

    reader = PdfReader(pdf_in_memory)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + '\n'

    return(text)
        