from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel


class ExamSchema(BaseModel):
    id: int
    title: str
    description: str
    created_at: str
    last_updated_at: str


class PostExamSchema(BaseModel):
    title: str
    description: str


app = FastAPI()

EXAMS = [{
        "created_at": "2018-02-21T15:32:13.188803+00:00",
        "description": "Test your knowledge with SQLAlchemy",
        "id": 1.0,
        "last_updated_by": "script",
        "title": "SQLAlchemy Exam",
        "updated_at": "2018-02-21T15:32:13.188823+00:00"
    },
        {
            "created_at": "2018-02-21T15:36:04.431399+00:00",
            "description": "Tricky questions about Typescript",
            "id": 2.0,
            "last_updated_by": "HTTP POST request",
            "updated_at": "2018-02-21T15:36:04.431417+00:00"
        }
    ]


@app.get("/exams")
async def get_exams():
    return EXAMS


@app.post("/exams")
async def add_exam(exam: PostExamSchema):
    dictionary = exam.dict()
    dictionary.update({"id": len(EXAMS) + 1,
                       "updated_at": "2020-05-09T15:36:04.431417+00:00",
                       "last_updated_by": "HTTP POST Request"})
    EXAMS.append(dictionary)
    return exam
