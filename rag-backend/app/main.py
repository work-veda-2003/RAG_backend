from fastapi import FastAPI
from app.ingestion import ingest_document
from app.retriever import retrieve
from app.generator import generate_answer

app = FastAPI()

@app.post("/ingest")
def ingest(text: str):
    ingest_document(text)
    return {"status": "ingested"}

@app.get("/query")
def query(q: str):
    context = retrieve(q)
    answer = generate_answer(q, "\n".join(context))
    return {"answer": answer}