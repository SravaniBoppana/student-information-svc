from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return [
        {
            "student_id": "S001",
            "name": "Alice Johnson",
            "email": "alice.johnson@example.com",
            "course_id": "CSE101",
            "course_name": "Intro to Computer Science",
            "last_activity": "2025-07-09T10:00:00Z",
            "engagement_time": 90
        },
        {
            "student_id": "S002",
            "name": "Bob Smith",
            "email": "bob.smith@example.com",
            "course_id": "CSE101",
            "course_name": "Intro to Computer Science",
            "last_activity": "2025-07-09T11:30:00Z",
            "engagement_time": 120
        }
    ]
