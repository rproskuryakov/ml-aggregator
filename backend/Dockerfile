FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6
LABEL maintainer="rodion43pv@gmail.com>"

WORKDIR /app
COPY app/requirements.txt /app
RUN pip install -r requirements.txt
EXPOSE 8000