import json


def create_api_gateway_response(body, status_code=200, headers=None):
    """
    Create an API Gateway response format for AWS Lambda.

    Parameters:
    - body: The response body (a dictionary).
    - status_code: The HTTP status code (default is 200).
    - headers: Optional headers for the response (default is None).

    Returns:
    A dictionary representing the API Gateway response.
    """
    response = {
        'statusCode': status_code,
        'body': json.dumps(body),
    }

    if headers:
        response['headers'] = headers

    return response