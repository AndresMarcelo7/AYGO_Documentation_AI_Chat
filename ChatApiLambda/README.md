# Chat API Lambda

In this project, you will find the code to use vector databases (Elasticsearch and Pinecone) combined with the OpenAI LLM model as an API to chat with information stored in the databases.

## Requirements

To run this project, you need:

- Python
- Docker
- AWS Account (For deployment with Api Gateway)
- OpenAI Api Key
- Elasticsearch API Key
- Pinecone API Key

## Local Execution:

1. To run the project locally, you need to have the following environment variables configured on your system:
   - ELASTIC_API_KEY
   - ELASTIC_CLOUD_ID
   - OPENAI_API_KEY
   - PINECONE_API_KEY
   - PINECONE_ENV
2. Create a virtual environment
   ```shell
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Download the requirements: ````pip install -r requirements.txt````.
4. Run the [test.py](test.py) file ```python test.py```

This test script simulates an API Gateway event as if it were a real request and points to the configured endpoint, which can be changed at any time for testing purposes.

## Evidence

The deployed API on AWS looks as follows:

![awsapigateway.png](..%2Fimg%2Fawsapigateway.png)