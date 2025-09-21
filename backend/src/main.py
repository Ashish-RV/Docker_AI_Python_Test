from fastapi import FastAPI 
import os

app = FastAPI()
MY_PROJECT = os.environ.get("MY_PROJECT")
API_KEY= os.environ.get("API_KEY")
if not API_KEY:
    raise NotImplementedError("API Key is missing")

@app.get("/")
def read_index():
    return {"hello":"Message3", "Project Name": MY_PROJECT}