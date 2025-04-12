from dotenv import load_dotenv
import os

load_dotenv()

API_KEY_openai = os.getenv("API_KEY_openai")
API_KEY_langsmith = os.getenv("API_KEY_langsmith")