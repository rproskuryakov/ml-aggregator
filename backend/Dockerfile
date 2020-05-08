FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

WORKDIR /app
COPY app/requirements.txt /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]