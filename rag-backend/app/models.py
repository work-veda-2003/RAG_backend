from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    id = Column(Integer, primary_key=True)
    content = Column(Text)
    metadata = Column(String)