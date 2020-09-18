import os
from typing import List
from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient


class ExamSchema(BaseModel):
    id: int
    title: str
    description: str
    updated_at: str
    last_updated_by: str


class PostExamSchema(BaseModel):
    title: str
    description: str
    long_description: str


class ArticleSchema(BaseModel):
    name: str
    abstract: str
    articleUrl: str
    source: str
    research_areas: List[str]
    date: str
    summary: str


MONGO_HOST = os.environ.get('MONGO_HOST', 'database')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'secret')
MONGO_USER = os.environ.get('MONGO_USER', 'mongo')

app = FastAPI()

client = AsyncIOMotorClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}",
                            username=MONGO_USER,
                            password=MONGO_PASSWORD,
                            authSource='mlDatabase',
                            authMechanism='SCRAM-SHA-256')

app.db = client.mlDatabase

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:4200",
    "http://localhost:4201",
    "http://127.0.0.1:4201",
    "http://127.0.0.1:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/articles")
async def get_articles() -> List[ArticleSchema]:
    articles = []
    cursor = app.db.articles.find()
    for article in await cursor.to_list(length=10):
        article.pop('_id')
        articles.append(article)
    return articles


@app.post("/articles")
async def add_exam(exam: PostExamSchema):
    dictionary = exam.dict()
    dictionary.update({"id": await app.db.exams.count_documents({}) + 1,
                       "updated_at": "2020-05-09T15:36:04.431417+00:00",
                       "last_updated_by": "HTTP POST Request"})
    await app.db.exams.insert_one(dictionary)
    return exam
