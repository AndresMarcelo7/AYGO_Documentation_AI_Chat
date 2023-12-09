from fastapi import FastAPI
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
import uvicorn
from langchain.vectorstores import Pinecone
import os
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

from config import openai_api_key

embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)

pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),  # find at app.pinecone.io
    environment=os.getenv("PINECONE_ENV"),  # next to api key in console
)
index_name = "pinecone-index"

docsearch = Pinecone.from_existing_index(index_name, embedding)
llm = OpenAI(temperature=0, openai_api_key=os.environ['OPENAI_API_KEY'])
chain = load_qa_chain(llm, chain_type="stuff")

app = FastAPI()


@app.get("/")
def index():
    return {
        "message": "Make a post request to /ask to ask questions about Meditations by Marcus Aurelius"
    }


@app.post("/ask")
def ask(query: str):
    docs = docsearch.similarity_search(query)
    answer = chain.run(input_documents=docs, question=query)
    return {
        "response": answer,
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)