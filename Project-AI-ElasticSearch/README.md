# Project AI Elastisearch

In this project you can run the indexer that downloads markdown documentation files from a s3 bucket, vectorize them and upload them to a database. 
vector Elasticsearch.

## Requirements

- Elasticsearch API KEY 
- Docker 
- Python
- AWS Account and Credentials

## Structure

This project contains:

- [indexer.py](src%2Findexer.py) Script in charge of downloading markdown documents and uploading them to a Pinecone vector database.
- [app.py](src%2Fapp.py) Local API in fastapi that allows to make direct requests to the database using an OpenAI LLM (Tests)
- [Dockerfile](Dockerfile) Containerized indexer for ease of execution

## Local execution
1. Set environment variables needed for AWS connection (AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,AWS_SESSION_TOKEN), S3 Data location (S3_BUCKET_NAME,S3_DATA_PREFIX) ,OpenAI (OPENAI_API_KEY) and Elasticsearch database connection (ELASTIC_API_KEY,ELASTIC_CLOUD_ID).
2. Create a virtual environment
``` shell
python3 -m venv .venv
source .venv/bin/activate
```
3. Download the requirements: ````pip install -r requirements.txt````.
3. Run the indexer ````pyhton indexer.py````

## Running with docker
1. To run the program just build the image of the [Dockerfile](Dockerfile) as follows:
```shell
docker build -t elasticsearch_indexer .
```

2. Run the docker image as follows including the necessary environment variables as shown below:
```shell
docker run  --env=AWS_ACCESS_KEY_ID=[ACCES_KEY] --env=AWS_SECRET_ACCESS_KEY=[SECRET_KEY] --env=AWS_SESSION_TOKEN=[SESSION_TOKEN] --env=OPENAI_API_KEY=[OPENAI_KEY] --env=PYTHONUNBUFFERED=1 --env=S3_BUCKET_NAME=[BUCKET_NAME] --env=S3_DATA_PREFIX=[BUCKET_PREFIX] --env=ELASTIC_API_KEY=[ELASTIC_KEY] --env=ELASTIC_CLOUD_ID=[ELASTIC_CLOUDID] --env=PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin --env=LANG=C.UTF-8 --env=GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D --env=PYTHON_VERSION=3.11.6 --env=PYTHON_PIP_VERSION=23.2.1 --env=PYTHON_SETUPTOOLS_VERSION=65.5.1 --env=PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/4cfa4081d27285bda1220a62a5ebf5b4bd749cdb/public/get-pip.py --env=PYTHON_GET_PIP_SHA256=9cc01665956d22b3bf057ae8287b035827bfd895da235bcea200ab3b811790b6  --workdir=/usr/app/src --add-host host.docker.internal:host-gateway -t -d elasticsearch_indexer
```
