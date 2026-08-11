"""
Streaming: Demonstrates streaming responses from the bedrock-mantle
endpoint using the Chat Completions API. Tokens are printed as they arrive.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

print("Streaming response from bedrock-mantle...\n")

stream = client.chat.completions.create(
    model="openai.gpt-oss-120b",
    messages=[
        {"role": "user", "content": "Explain serverless computing in 3 bullet points."}
    ],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)

print("\n\nDone.")
