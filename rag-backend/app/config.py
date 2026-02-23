import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATABASE_URL = "postgresql://rag:rag@postgres:5432/ragdb"
REDIS_HOST = "redis"