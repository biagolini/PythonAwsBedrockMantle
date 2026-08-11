"""
Responses API: Demonstrates stateful multi-turn conversations using the
bedrock-mantle Responses API. The endpoint stores conversation state for
30 days, so follow-up requests don't need the full history.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

print("Responses API - Stateful Multi-Turn Conversation Demo")
print("=" * 55)
print()
print("This script sends two sequential requests to bedrock-mantle.")
print("The second request references the first one via previous_response_id,")
print("so the model remembers the conversation without resending history.")
print()
print("=== Turn 1: Initial question ===")
print("Waiting for response (this may take a few seconds)...\n")

response = client.responses.create(
    model="openai.gpt-oss-120b",
    input=[
        {"role": "user", "content": "What are the main benefits of Amazon Bedrock?"}
    ]
)

print(response.output_text)
print(f"\n[Response ID: {response.id}]")

print("\n=== Turn 2: Follow-up (using previous_response_id) ===")
print("Waiting for response...\n")

follow_up = client.responses.create(
    model="openai.gpt-oss-120b",
    previous_response_id=response.id,
    input=[
        {"role": "user", "content": "Can you elaborate on the security aspect?"}
    ]
)

print(follow_up.output_text)
print(f"\n[Response ID: {follow_up.id}]")

print("\n\nDone. Both turns used the same conversation context without resending history.")
