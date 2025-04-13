import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def create_client():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    return client



