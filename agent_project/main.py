import os
from dotenv import load_dotenv
import openai
from initial_setups import create_client

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = create_client()


response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "I am talking to you from an application, do you read me?!"}]
)

print(response.choices[0].message.content)
