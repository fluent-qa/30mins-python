import os

from dotenv import load_dotenv
from langchain.adapters import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
CHROMA_PATH = "chroma"
DATA_PATH = "data/books"
