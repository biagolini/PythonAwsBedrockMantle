"""
List Models: Discovers available models on the bedrock-mantle endpoint.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

print("Available models on bedrock-mantle:\n")

models = client.models.list()
for model in models.data:
    print(f"  - {model.id}")

print(f"\nTotal: {len(models.data)} models")
