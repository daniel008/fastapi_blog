from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
    {
        "id": 3,
        "author": "Alex Johnson",
        "title": "Building REST APIs with FastAPI",
        "content": "FastAPI makes it easy to build modern REST APIs with automatic validation, serialization, and interactive documentation.",
        "date_posted": "April 22, 2025",
    },
    {
        "id": 4,
        "author": "Emily Chen",
        "title": "Getting Started with Python Backend Development",
        "content": "Learning FastAPI is a great way to start building backend applications using Python, type hints, and Pydantic.",
        "date_posted": "April 23, 2025",
    },
]


@app.get("/", response_class=HTMLResponse)
@app.get("/posts", response_class=HTMLResponse)
def home():
    return f"<h1>{posts[0]['title']}</h1>"


@app.get("/api/posts")
def get_posts():
    return posts
