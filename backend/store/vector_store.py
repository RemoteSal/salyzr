import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)
documents = []

def embed(texts):
    return model.encode(texts)

def add_documents(texts, metadata):
    embeddings = embed(texts)
    index.add(np.array(embeddings))
    for t, m in zip(texts, metadata):
        documents.append({"content": t, **m})

    print("--debug documents------", len(documents))

def search(query, k):
    q_emb = embed([query])
    print("\n\n--debug documents------", documents,"\n\n")
    _, idxs = index.search(np.array(q_emb), k)
    return [documents[i] for i in idxs[0]]


def enhanced_search(query, k):
    if len(documents) == 0:
        return []

    k = min(k, len(documents))
    q_emb = embed([query])
    _, idxs = index.search(np.array(q_emb), k)

    return [documents[i] for i in idxs[0] if i < len(documents)] or ["No documents found"]

