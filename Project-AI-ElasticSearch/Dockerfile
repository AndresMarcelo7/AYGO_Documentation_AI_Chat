FROM python:3.11
WORKDIR /usr/app
COPY . .
RUN pip install -r requirements.txt
WORKDIR /usr/app/src
CMD ["python","indexer.py"]