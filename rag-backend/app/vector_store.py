import faiss
import numpy as np
import pickle
import os

DIM = 1536
INDEX_FILE = "faiss.index"
META_FILE = "faiss_meta.pkl"

if os.path.exists(INDEX_FILE):
    index = faiss.read_index(INDEX_FILE)
    with open(META_FILE, "rb") as f:
        id_map = pickle.load(f)
else:
    index = faiss.IndexFlatL2(DIM)
    id_map = {}

def add_vector(vector, doc_id):
    vec = np.array([vector]).astype("float32")
    index.add(vec)
    id_map[index.ntotal - 1] = doc_id
    save()

def search(vector, k=5):
    vec = np.array([vector]).astype("float32")
    distances, indices = index.search(vec, k)
    return [id_map[i] for i in indices[0]]

def save():
    faiss.write_index(index, INDEX_FILE)
    with open(META_FILE, "wb") as f:
        pickle.dump(id_map, f)