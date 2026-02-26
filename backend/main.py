from fastapi import FastAPI
from backend.agent import ask_agent

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "Titanic Chat Agent running"}

@app.get("/ask")
def ask(q: str):
    res = ask_agent(q)
    return {"answer": res}