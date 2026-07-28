from __future__ import annotations

from pathlib import Path
from config import RAG_CHUNK_OVERLAP, RAG_CHUNK_SIZE, RAG_COLLECTION, RAG_PERSIST_DIR


def _chunks(text: str) -> list[str]:
    text = " ".join(text.split())
    if not text:
        return []
    chunks = []
    start = 0
    while start < len(text):
        end = min(len(text), start + RAG_CHUNK_SIZE)
        chunks.append(text[start:end])
        if end == len(text):
            break
        start = max(0, end - RAG_CHUNK_OVERLAP)
    return chunks


def _collection():
    import chromadb
    Path(RAG_PERSIST_DIR).mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=RAG_PERSIST_DIR)
    return client.get_or_create_collection(RAG_COLLECTION)


def add_document(text: str, source: str) -> int:
    chunks = _chunks(text)
    if not chunks:
        return 0

    collection = _collection()
    import uuid
    ids = [str(uuid.uuid4()) for _ in chunks]
    collection.add(
        ids=ids,
        documents=chunks,
        metadatas=[{"source": source, "chunk": i} for i in range(len(chunks))],
    )
    return len(chunks)


def search_documents(query: str, top_k: int = 5) -> list[dict]:
    if not query.strip():
        return []
    collection = _collection()
    if collection.count() == 0:
        return []

    result = collection.query(
        query_texts=[query],
        n_results=max(1, min(top_k, 10)),
    )
    docs = result.get("documents", [[]])[0]
    metas = result.get("metadatas", [[]])[0]
    distances = result.get("distances", [[]])[0]

    return [
        {
            "text": doc,
            "source": meta.get("source"),
            "chunk": meta.get("chunk"),
            "distance": distance,
        }
        for doc, meta, distance in zip(docs, metas, distances)
    ]
