from fastapi import FastAPI 
import os
from contextlib import asynccontextmanager
from api.db import init_db
from api.chat.routing import router as chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(chat_router, prefix="/api/chats")
MY_PROJECT = os.environ.get("MY_PROJECT")
API_KEY= os.environ.get("API_KEY")
if not API_KEY:
    raise NotImplementedError("API Key is missing")


@app.get("/")
def read_index():
    return {"hello":"Message3", "Project Name": MY_PROJECT}