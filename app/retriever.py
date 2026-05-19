from app.document_loader import load_text_documents
from app.chunking import split_documents_into_chunks
from app.vector_store import VectorStore


_vector_store = VectorStore()
_index_ready = False


def ingest_documents():
    """
    Loads documents, splits them into chunks, and indexes them in FAISS.
    """
    global _index_ready

    documents = load_text_documents()
    chunks = split_documents_into_chunks(documents)

    result = _vector_store.build_index(chunks)
    _index_ready = True

    return result


def retrieve_relevant_chunks(question: str, top_k: int = 3):
    """
    Retrieves relevant chunks for a user question.
    """
    global _index_ready

    if not _index_ready:
        ingest_documents()

    results = _vector_store.search(question, top_k=top_k)

    return results