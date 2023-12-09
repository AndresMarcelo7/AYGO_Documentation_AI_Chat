FROM public.ecr.aws/lambda/python:3.11
COPY /handlers ./handlers
COPY /utils ./utils
COPY lambda_function.py .
COPY requirements.txt .
COPY test.py .
RUN pip install -r requirements.txt
CMD ["lambda_function.lambda_handler"]