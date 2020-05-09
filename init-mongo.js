db.createUser(
    {
        user: "mongo",
        pwd: "secret",
        roles: [
            {
                role: "readWrite",
                db: "mlDatabase"
            }
        ]
    }
)
db.exams.insertMany(
    [
        {
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
            "title": "Typescript Exam",
            "last_updated_by": "HTTP POST request",
            "updated_at": "2018-02-21T15:36:04.431417+00:00"
        }
    ]
)