import fastapi
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise
import sys

sys.path.append("..")

from app.src.database.register import register_tortoise
from app.src.database.config import TORTOISE_ORM

# enable schemas to read relationship between models
Tortoise.init_models(["src.database.models"], "models")

# import 'from src.routes' must be after 'Tortoise.init'
from app.src.routes import users, notes

app = fastapi.FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users.router)
app.include_router(notes.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

@app.get("/")
def read_root():
    return "Hello, World!"
