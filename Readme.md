# Multi-Agent Research Paper Processor


## Setup Instructions (Dockerized application)


1. Pull Docker Image
```bash
docker pull iverant/vahanai-research-paper-processor:latest
```

2. Run docker image
```bash
docker run -it -p 8501:8501 iverant/vahanai-research-paper-processor:latest
```

3. Open your web browser and navigate to:
```bash
http://0.0.0.0:8501 or http://localhost:8501
```

4. Deployed Project Link (Direct Access)
```
https://multi-agent-research-paper-processor.onrender.com
```

## Demo

You can access the website via the link given above.

Photos:

1. User input Topics for classification

![image]([https://private-user-images.githubusercontent.com/132095775/433063564-ffd88909-a367-4867-9eab-5990c931bfd3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDQ0Nzg0NjcsIm5iZiI6MTc0NDQ3ODE2NywicGF0aCI6Ii8xMzIwOTU3NzUvNDMzMDYzNTY0LWZmZDg4OTA5LWEzNjctNDg2Ny05ZWFiLTU5OTBjOTMxYmZkMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDEyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQxMlQxNzE2MDdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kMWMyYjg0NjhmMTJhOTlmN2IwYjgwYWIxZjdhNWFjMTA2MWY0MTQ2MzVmMWViNDY1MDFlNDg3OTdiYTVlMGU0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.g9HOTkCLQQSEgDc11WgXPKcE8QclYXlsrYkb7VUZJWY](https://github.com/Iverant/Images/blob/master/Picture2.png?raw=true))

2. Research Paper Search Results

![image]([https://private-user-images.githubusercontent.com/132095775/433063652-1acf3617-7cdc-4f03-9b39-9608b57c241e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDQ0Nzg2NzUsIm5iZiI6MTc0NDQ3ODM3NSwicGF0aCI6Ii8xMzIwOTU3NzUvNDMzMDYzNjUyLTFhY2YzNjE3LTdjZGMtNGYwMy05YjM5LTk2MDhiNTdjMjQxZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDEyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQxMlQxNzE5MzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xNDJiNjUzYjAwOTc2NzFhNjJlNjdmNDljZTA4ZTA3ZmM3NDc3NDc1MGIzYjBiMmFhNDc1YjM1OTcxZTFlMGZjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.FpUoTZGy53oyJyP5VkR8YhISUCDJeaOb5b2excx8IGs](https://github.com/Iverant/Images/blob/master/Picture3.png?raw=true))

3. Pdf Handler

![image]([https://private-user-images.githubusercontent.com/132095775/433064593-8ff499be-b913-4dd3-8120-511028a6fd4e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDQ0Nzg3NDgsIm5iZiI6MTc0NDQ3ODQ0OCwicGF0aCI6Ii8xMzIwOTU3NzUvNDMzMDY0NTkzLThmZjQ5OWJlLWI5MTMtNGRkMy04MTIwLTUxMTAyOGE2ZmQ0ZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDEyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQxMlQxNzIwNDhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03NzM4YjE2YmYyMGFkODE4ZjQ0ZTU1NTgzZmExMDJjNmU3MGRlN2IwMGMxOWRkZGMzZDcwMTI0YzU1NzBmMGFlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.U69VWVcPPkcSmf2DQIfd42atC3P1bv01eHLkI9a9BKg](https://github.com/Iverant/Images/blob/master/Picture4.png?raw=true))


4. URL Handler

![image]([https://private-user-images.githubusercontent.com/132095775/433064657-4f6590a1-8244-42ec-8ac4-57be1ef60ea9.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDQ0Nzg4MDQsIm5iZiI6MTc0NDQ3ODUwNCwicGF0aCI6Ii8xMzIwOTU3NzUvNDMzMDY0NjU3LTRmNjU5MGExLTgyNDQtNDJlYy04YWM0LTU3YmUxZWY2MGVhOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDEyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQxMlQxNzIxNDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hZjBjMTNhMTk3NjAzYzcxNDYwOWU4OGE4YjNmYmI1Y2IyMTFiN2JjMmQ3ZmZlN2JmNmFjNjBlNmQ2ODAyODY2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.BT3KGw-RrrYQPTQo-v1ICrIn0D6eKJChrqemDYl5dIE](https://github.com/Iverant/Images/blob/master/Picture5.png?raw=true))

5. Results (Topic Classification, Summary, Audio output)

![image]([https://private-user-images.githubusercontent.com/132095775/433064737-b4ca46dd-3021-4800-b53a-9016cb52343c.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDQ0Nzg4ODYsIm5iZiI6MTc0NDQ3ODU4NiwicGF0aCI6Ii8xMzIwOTU3NzUvNDMzMDY0NzM3LWI0Y2E0NmRkLTMwMjEtNDgwMC1iNTNhLTkwMTZjYjUyMzQzYy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDEyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQxMlQxNzIzMDZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04MzVmMzNiMjQyMzk3OTI5Zjc5ZTBjOWMwNzQ5MTQyNmU5ODUyNjQxZTQ3YTA5NjI3MzM3ZjkwMWVjM2FjNTc2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.yde1v56hC96LkdEs4gTTxwnDfMErmI0TTgLT5s9iaB4](https://github.com/Iverant/Images/blob/master/Picture6.png?raw=true))


## System Architecture

The system is organized into modular components, each responsible for a specific task. The directory structure is as follows:

```
VahanAI/
│
├── app.py                          # Streamlit web interface
├── main.py                         # Command-line interface
├── keys.py                         # API keys
├── agents/                         # Specialized agents
│   ├── paper_search.py             # Paper search and discovery
│   ├── topic_and_summary.py        # Topic classification and summarization
│   ├── audio.py                    # Audio generation
│   └── .env                        # Environment variables
│
├── utils/                          # Utility functions
│   ├── pdf_loader.py               # Local PDF processing
│   ├── url_loader.py               # URL-based PDF processing
│
├── outputs/                        # Generated outputs
│   ├── summaries/                  # Text summaries
│   └── audio/                      # Audio podcasts
│
└── requirements.txt                # Python dependencies
```


## Multi-Agent Design and Coordination Approach

The system employs a multi-agent architecture, where each agent is specialized for a specific task. These agents work together in a pipeline to process research papers from input to output.

Agents

1. Paper Search Agent `paper_search.py`:

    - Interfaces with the Semantic Scholar API to search for research papers.
    - Retrieves metadata such as title, URL, and PDF link.

2. Document Processing Agents:

    - PDF Loader `pdf_loader.py`: Extracts text from local PDF files.
    - URL Loader `url_loader.py`: Downloads and extracts text from PDFs hosted online.
3. Topic Classification Agent `topic_and_summary.py`:

    - Uses an LLM to classify papers into user-defined topics.
    - Employs a prompt-based approach for accurate classification.

4. Summary Generation Agent `topic_and_summary.py`:

    Generates structured summaries with sections for:
    - Objective
    - Methods
    - Results
    - Limitations
    - Future Work

    Uses LangChain's refine-based summarization chain.

5. Audio Generation Agent `audio.py`:

    Converts text summaries into audio podcasts using Google Text-to-Speech (gTTS).

Coordination

The main orchestrator `main.py` or `app.py` coordinates the agents:

- Accepts user input (search query, PDF upload, or URL).
- Passes the input to the appropriate agent for processing.
- Collects intermediate outputs (e.g., text content, classification, summary).
- Generates final outputs (e.g., summaries, audio files).
- Displays results in the web interface or saves them to the `outputs/` directory.

## Paper processing methodology

Input Methods

1. Search:

    - Users can search for papers using a query.
    - The system retrieves papers via the Semantic Scholar API.

2. PDF Upload:

    - Users can upload local PDF files for processing.

3. URL Input:

    - Users can provide a URL to a PDF hosted online.

Processing Steps

1. Text Extraction:

    - Local PDFs are processed using LangChain's `PyPDFLoader`.
    - Online PDFs are downloaded and processed using `PyPDF2`.

2. Topic Classification:

    - The first 5000 characters of the extracted text are analyzed.
    - The LLM classifies the paper into one of the user-defined topics.

3. Summary Generation:

    - The text is split into manageable chunks (3000 characters with 200-character overlap).
    - A refine-based summarization chain generates a structured summary.

4. Output Generation:

    - Summaries are saved as `.txt` files in the `outputs/`summaries/ directory.
    - Audio podcasts are saved as .mp3 files in the `outputs/audio/` directory.

## Audio Generation Summary

The audio generation agent `audio.py` converts text summaries into audio files:

1. Input:

    - The structured summary generated by the summarization agent.

2. Processing:

    - The text is passed to Google Text-to-Speech (gTTS).
    - The audio is generated in MP3 format.

3. Output:

    - The audio file is saved in the outputs/audio/ directory.
    - The web interface provides playback and download options.

## Limitations and Future Improvements

Current Limitations

1. API Dependence:

    - Relies on external APIs (Semantic Scholar, OpenAI, LangSmith), which may have rate limits or downtime.

2. PDF Processing:

    - Struggles with complex layouts, scanned documents, or non-standard formatting.

3. Language Support:

    - Currently limited to English for both text and audio.

4. Audio Quality:

    - Basic text-to-speech without advanced voice modulation or natural speech patterns.

5. Cross-Paper Analysis:

    - Each paper is processed independently; lacks synthesis across multiple papers.

Future Improvements

1. Enhanced PDF Processing:

    - Support for extracting structured data (e.g., tables, figures).
    - Improved handling of multi-column layouts and scanned documents.

2. Expanded Data Sources:

    - Integrate additional academic repositories (e.g., PubMed, arXiv).
    - Support for DOI-based paper retrieval.

3. Cross-Paper Synthesis:

    - Generate insights across multiple papers on the same topic.
    - Create literature review summaries.

4. Improved Audio Generation:

    - Add multiple voice options and styles.
    - Incorporate natural speech patterns with pauses and emphasis.

5. User Experience Enhancements:

    - Add user accounts for saving and revisiting processed papers.
    - Provide citation export in various formats (e.g., APA, MLA).
    - Develop a mobile app for on-the-go access.

6. Scalability:

    - Enable batch processing for large datasets.
    - Implement caching to avoid redundant processing.
