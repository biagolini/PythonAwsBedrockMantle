# Amazon Bedrock Mantle - Hello World

**Author:** Carlos Biagolini-Jr.

**LinkedIn:** [https://www.linkedin.com/in/biagolini/](https://www.linkedin.com/in/biagolini/)

**Medium:** [https://medium.com/@biagolini](https://medium.com/@biagolini)

## Overview

This project demonstrates how to use the [Amazon Bedrock Mantle endpoint](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-mantle.html) (`bedrock-mantle`) with the OpenAI Python SDK. The `bedrock-mantle` endpoint provides an OpenAI-compatible API, allowing you to use familiar OpenAI SDKs with Amazon Bedrock models by simply changing the base URL and API key.

The project includes examples for:

- Listing available models
- Chat Completions API (basic request)
- Responses API (stateful multi-turn conversations)
- Streaming responses

## Prerequisites

- AWS account with Amazon Bedrock access
- IAM identity with `AmazonBedrockMantleInferenceAccess` managed policy (or equivalent custom policy)
- Python 3.9+ installed
- A Bedrock API key generated from the [Amazon Bedrock Console](https://console.aws.amazon.com/bedrock/home#/api-keys)

## Setup

1. Clone this repository:

```bash
git clone https://github.com/biagolini/PythonAwsBedrockMantle.git
cd PythonAwsBedrockMantle
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Copy the example environment file and edit with your values:

```bash
cp .env.example .env
```

Edit `.env`:

```
OPENAI_BASE_URL=https://bedrock-mantle.us-east-1.api.aws/v1
OPENAI_API_KEY=<your-bedrock-api-key>
```

Replace `<your-bedrock-api-key>` with the short-term or long-term API key generated from the Amazon Bedrock Console.

## Usage

List available models:

```bash
python list_models.py
```

Run the Chat Completions example (hello world):

```bash
python hello_mantle.py
```

Run the Responses API example (stateful conversation):

```bash
python responses_api.py
```

Run the streaming example:

```bash
python streaming.py
```

Verify the endpoint with cURL (no Python required):

```bash
./curl_chat_completions.sh
```

## Project Structure

```
.
├── .env.example              # Template for environment variables
├── .gitignore
├── requirements.txt          # Python dependencies
├── list_models.py            # List available models on bedrock-mantle
├── hello_mantle.py           # Chat Completions API - basic hello world
├── responses_api.py          # Responses API - stateful multi-turn conversation
├── streaming.py              # Streaming responses example
├── curl_chat_completions.sh  # cURL verification (no Python needed)
├── LICENSE
└── README.md
```

## Cleanup

After testing, remember to:

- Revoke or let your short-term API key expire (automatic after max 12 hours)
- If you created a long-term API key, delete it from the Bedrock Console or via IAM

## Contributing

Feel free to submit issues and pull requests.

## License

This project is open source and available under the [MIT License](LICENSE).
