FROM python:3.6-slim-stretch
LABEL maintainer="rodion43pv@gmail.com>"

WORKDIR /usr/app/

COPY ./crawler .
COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir /etc/scrapyd/ \
    && echo "[scrapyd] \n bind_address = 0.0.0.0" > /etc/scrapyd/scrapyd.conf

EXPOSE 6800