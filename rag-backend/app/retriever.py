from app.embedding import embed_text
from app.vector_store import search
from app.database import SessionLocal
from app.models import DocumentChunk

def retrieve(query: str):
    embedding = embed_text(query)
    doc_ids = search(embedding)

    db = SessionLocal()
    docs = db.query(DocumentChunk).filter(
        DocumentChunk.id.in_(doc_ids)
    ).all()
    return [d.content for d in docs]