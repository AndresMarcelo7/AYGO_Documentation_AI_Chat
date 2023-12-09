import json

from handlers import pinecone_handler, elastic_handler
from utils.response_utils import create_api_gateway_response


def lambda_handler(event,context):
    body = json.loads(event["body"])
    if event["path"] == "/pinecone":
        return pinecone_handler.handle(body["message"])
    elif event["path"] == "/elastic":
        return elastic_handler.handle(body["message"])
    else:
        return create_api_gateway_response("Not Found", 404)


