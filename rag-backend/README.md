# RAG Backend (Fully Local)

A fully local Retrieval-Augmented Generation (RAG) backend system designed to ingest document collections and answer queries using hybrid retrieval and context-grounded generation.

OpenAI API is intentionally not used. The system runs entirely on open-source models to avoid external dependencies and usage costs.

---

## Overview

This project implements a modular RAG pipeline consisting of:

- Document ingestion and preprocessing
- Semantic chunking
- Embedding generation
- Hybrid retrieval (dense + keyword)
- Context-grounded response generation
- REST API exposure

The system operates fully locally using open-source components.

---

## Tech Stack

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

## Architecture

### Ingestion Pipeline

Documents  
→ Chunking  
→ Embedding Generation  
→ FAISS Index + BM25 Index  
→ Metadata Storage  

### Query Pipeline

User Query  
→ Query Embedding  
→ Hybrid Retrieval  
→ Context Assembly  
→ LLM Generation  
→ Response  

---

## Retrieval Strategy

- Dense vector search using FAISS with HNSW indexing
- Keyword-based ranking using BM25
- Weighted hybrid score combination
- Top-k context filtering before generation

---

## Hallucination Control

- LLM instructed to use only retrieved context
- Fallback response when supporting context is insufficient
- Context strictly assembled from retrieval layer

---

## Evaluation

Supports quantitative evaluation using:

- Recall@k
- Precision@k
- Context relevance scoring
- Basic hallucination detection

---

## Design Decisions

- Fully local inference to remove external API dependency
- HNSW indexing for scalable approximate nearest neighbor search
- Hybrid retrieval to balance semantic similarity and lexical precision
- Modular backend structure for scalability and maintainability

---

## Running the Application

Start the API server:

```bash
uvicorn app.main:app --reload
