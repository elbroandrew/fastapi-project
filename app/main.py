import fastapi
from fastapi.middleware.cors import CORSMiddleware

from app.src.database.register import register_tortoise
from app.src.database.config import TORTOISE_ORM

app = fastapi.FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

@app.get("/")
def read_root():
    return "Hello, World!"

@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}
