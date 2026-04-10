from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Changed model to a standard one, adjust if needed
    messages=[
        {"role": "system", "content": "You are a chatbot that only answers questions about Python programming. If the query is not related to Python, respond with 'I can only assist with Python programming questions.'"},
        {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}
    ]
)

print(response.choices[0].message.content)