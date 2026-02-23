from app.embedding import embed_text
from app.vector_store import add_vector
from app.database import SessionLocal
from app.models import DocumentChunk

def ingest_document(text):
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]

    db = SessionLocal()

    for chunk in chunks:
        doc = DocumentChunk(content=chunk)
        db.add(doc)
        db.commit()
        db.refresh(doc)

        embedding = embed_text(chunk)
        add_vector(embedding, doc.id)