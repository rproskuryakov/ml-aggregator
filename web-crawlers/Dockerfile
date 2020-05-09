FROM python:3.6-slim-stretch

WORKDIR /usr/app/

COPY ./crawler .
COPY requirements.txt .

RUN pip install -r requirements.txt