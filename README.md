# AYGO_Documentation_AI_Chat

Universidad Escuela Colombiana de Ingenieria Julio Garavito

# AYGO Final Project: AI Chat with Custom Organization Repositories

## Team Members:
- Andres Felipe Marcelo
- Juan Camilo Rojas
- Juan Camilo Angel

## Repository Contents:

In this repository, you will find organized resources used for the development of the project as follows:
- [Project Paper](AYGO_2023-1.pdf): Paper of the project, it describes business case, methodology, results and future work.
- [Project-AI-ElasticSearch](Project-AI-ElasticSearch): Indexer Project (Data Loading) for Elasticsearch vector database.
- [Project-AI-Pinecone](Project-AI-Pinecone): Indexer Project (Data Loading) for Pinecone vector database.
- [ChatApiLambda](ChatApiLambda): AWS Lambda API protected with Cognito to establish conversations with Elasticsearch and Pinecone databases.
- [AYGO-Project-Chat.postman_collection.json](AYGO-Project-Chat.postman_collection.json): Postman collection for making requests to the deployed API with Api Gateway.

Each directory contains a README.MD detailing the objective of each and how to implement it locally.

## Objective:

In this project, we propose the use of long language models (LLMs) to address the challenge of complexity in understanding technical documentation. Given the effectiveness of these models in understanding and generating natural language, we suggest using them to provide developers with an expert agent. This agent, when trained on specific data from technical documentation, will enable them to ask questions and quickly comprehend the documentation.

With this project, our aim is to assess the feasibility of the proposed solution. To achieve this, we have designed a reference architecture outlining the desirable features of the solution. From this architecture, we have developed a prototype that implements a simplified version, including the key components. The objective is to conduct a proof of concept to validate its functionality. Subsequently, we plan to perform experiments with this prototype to evaluate the solution’s performance using two different vector databases.

## Architecture:

The proposed architecture for the proof of concept is as follows:
![PoCArchitecture.jpeg](img%2FPoCArchitecture.jpeg)

Here, the entry point to the service is an API Gateway + Lambda protected with Cognito OAuth2. This service connects directly to the vector databases of Elasticsearch or Pinecone depending on the endpoint and uses an OpenAI model to process and return a response according to the asked question.

For data loading, AWS Batch service and a Python algorithm (Indexer) are used to download all documentation files from an S3, vectorize them, and load them into the corresponding database (Pinecone or Elasticsearch).

## Requirements:

To replicate this project in your local environment, you need:
- AWS account
- OpenAI API Key
- Elasticsearch API KEY and CloudId
- Pinecone API KEY and Environment
- Docker
- Python > 3.10

## Local Environment Testing:
0. Clone the repository.
1. In your AWS account, create an S3 bucket where the documentation files will be stored.
2. Execute the search and data upload script to S3: `python3 <script_name>`
3. Using Docker, run the preferred indexer: [Elasticsearch indexer](Project-AI-ElasticSearch%2FREADME.md) or [Pinecone indexer](Project-AI-Pinecone%2FREADME.md).
4. Use the test script [test.py](ChatApiLambda%2Ftest.py), simulating an API Gateway event to Lambda and test the endpoint's response.

## Proof of Concept Results (Cloud Environment)

### Data Insertion
Tests were conducted on each database to determine the time it took to load and vectorize the data. The results are as follows:

For Elasticsearch, the data loading times are as follows:

| Run | Total Execution Time (seconds) |
|-----|--------------------------------|
| 1   | 720.0                          |
| 2   | 730.0                          |
| 3   | 722.5                          |
| 4   | 728.5                          |
| 5   | 724.0                          |
| AVG | 725.0                          |

For Pinecone, the data loading times are as follows:

| Run | Total Execution Time (seconds) | 
|-----|--------------------------------| 
| 1   | 680.0                          |
| 2   | 675.5                          | 
| 3   | 678.0                          | 
| 4   | 680.5                          | 
| 5   | 675.0                          | 
| AVG | 677.4                          | 

### Load Testing
Load tests were also conducted on the vector databases loaded with more than 3000 documents, each database having 7920 vectors of 1536 dimensions each.

#### Pinecone
For Pinecone, the following graph details the request behavior starting from 50 concurrent users up to 1000 concurrent users:
![PineconeLoadTest.jpeg](img%2FPineconeLoadTest.jpeg)

#### ElasticSearch
In the case of Elasticsearch, we observed that as the requests increased, the service became temporarily unavailable, suggesting that the service auto-scaled until it reached a limit of 700 concurrent users.
![ElasticsearchLoadTest.jpeg](img%2FElasticsearchLoadTest.jpeg)

### Deployed API Evidence
The documentation of the endpoints is in the collection [AYGO-Project-Chat.postman_collection.json](AYGO-Project-Chat.postman_collection.json). Still, evidence of calls to the 2 deployed endpoints in AWS and their protection with Cognito is also attached.

- #### Cognito Token 
![OauthRequest.png](img%2FOauthRequest.png)
- #### Elastic Query
![ElasticQuery.png](img%2FElasticQuery.png)
- #### Pinecone Query
![PineconeQuery.png](img%2FPineconeQuery.png)
- #### Unauthorized Query
![UnauthorizedQuery.png](img%2FUnauthorizedQuery.png)
