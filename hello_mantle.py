"""
Hello Mantle: Basic Chat Completions API example using the
bedrock-mantle endpoint with the OpenAI Python SDK.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

print("Sending request to bedrock-mantle (Chat Completions API)...\n")

response = client.chat.completions.create(
    model="openai.gpt-oss-120b",
    messages=[
        {"role": "user", "content": "Say hello and explain what Amazon Bedrock Mantle is in two sentences."}
    ]
)

print("Model:", response.model)
print("Usage:", f"{response.usage.prompt_tokens} input / {response.usage.completion_tokens} output tokens")
print("\n--- Response ---")
print(response.choices[0].message.content)
