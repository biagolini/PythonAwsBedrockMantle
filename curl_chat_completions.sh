#!/bin/bash
# curl_chat_completions.sh
# Sends a Chat Completions request to the bedrock-mantle endpoint using cURL.
# Useful for verifying the endpoint works without any Python setup.
#
# Usage: ./curl_chat_completions.sh

set -e

if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

if [ -z "$OPENAI_BASE_URL" ] || [ -z "$OPENAI_API_KEY" ]; then
    echo "Error: OPENAI_BASE_URL and OPENAI_API_KEY must be set in .env file"
    exit 1
fi

echo "Sending Chat Completions request to bedrock-mantle via cURL..."
echo "Endpoint: $OPENAI_BASE_URL/chat/completions"
echo ""

curl -s -X POST "$OPENAI_BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "openai.gpt-oss-120b",
    "messages": [
        {"role": "user", "content": "Hello from Bedrock Mantle! Reply in one sentence."}
    ]
  }' | python3 -m json.tool

echo ""
echo "Done."
