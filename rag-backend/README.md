# 🧠 RAG Backend (Fully Local)

A scalable, fully local Retrieval-Augmented Generation (RAG) backend system designed to ingest large document collections and answer queries with high factual grounding and minimal hallucination.

> ⚠️ Note: OpenAI API is intentionally not used because it is paid.  
> This system is fully local and cost-free using open-source models.

---
    
## 🚀 Tech Stack

| Layer          | Tool Used |
|---------------|-----------|
| API           | FastAPI |
| LLM           | Llama 3 (via Ollama) |
| Embeddings    | BGE-small / all-MiniLM |
| Vector Search | FAISS (HNSW) |
| Keyword Search| BM25 |
| Metadata      | SQLite / PostgreSQL |
| Container     | Docker |

---

## 🏗 Architecture

### Ingestion Pipeline
Documents → Chunking → Embeddings → FAISS + BM25 → Metadata Store

### Query Pipeline
User Query → Query Embedding → Hybrid Retrieval → Context Filtering → Llama 3 → Response

---

## 🔎 Key Engineering Decisions

- Hybrid search (Dense + BM25) to reduce semantic drift
- HNSW index for scalable vector retrieval
- Strict context-grounded prompting to control hallucination
- Modular backend structure for production scaling
- Fully local models to eliminate API cost and rate limits

---

## 📊 Evaluation

Supports:
- Recall@k
- Precision@k
- Context relevance scoring
- Hallucination detection

---

## 🛡 Hallucination Control

LLM is forced to:
- Use only retrieved context
- Return “Insufficient information” if unsupported

---

## 🎯 Why No OpenAI API?

OpenAI API is paid and rate-limited.  
This project is intentionally designed to be:

- Fully local
- Cost-free
- Scalable
- Production-ready

---

## 🧠 What This Demonstrates

- Retrieval system design
- Vector indexing optimization
- Hybrid ranking strategies
- Backend modular architecture
- Practical RAG production engineering

---

## ▶ Run Locally

```bash
uvicorn app.main:app --reload