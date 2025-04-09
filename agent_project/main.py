import os
from dotenv import load_dotenv
import openai

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=api_key)
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "I am talking to you from an application, do you read me?!"}]
)

print(response.choices[0].message.content)
