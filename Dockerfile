# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /clients-tests

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "pytest", "tests/test_clients.py", "-v" ]