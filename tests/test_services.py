from services.rag_service import _chunks


def test_chunking():
    text = "a" * 2500
    chunks = _chunks(text)
    assert len(chunks) >= 3
    assert all(chunks)
