from fastapi import FastAPI
from pydantic import BaseModel

from app.document_loader import load_text_documents
from app.chunking import split_documents_into_chunks
from app.retriever import ingest_documents
from app.rag_pipeline import run_rag_pipeline

app = FastAPI(
    title="Enterprise GenAI RAG Platform",
    description="A semantic document retrieval and RAG API for enterprise financial documents.",
    version="1.0.0"
)


class QueryRequest(BaseModel):
    question: str
    top_k: int = 3


@app.get("/")
def home():
    return {
        "message": "Enterprise GenAI RAG Platform is running successfully."
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "rag-platform"
    }


@app.get("/documents")
def get_documents():
    documents = load_text_documents()

    return {
        "total_documents": len(documents),
        "documents": [
            {
                "source": document["source"],
                "characters": len(document["content"])
            }
            for document in documents
        ]
    }


@app.get("/chunks")
def get_chunks():
    documents = load_text_documents()
    chunks = split_documents_into_chunks(documents)

    return {
        "total_chunks": len(chunks),
        "chunks": chunks
    }


@app.post("/ingest")
def ingest():
    result = ingest_documents()

    return {
        "message": "Documents indexed successfully.",
        "details": result
    }


@app.post("/query")
def query_documents(request: QueryRequest):
    result = run_rag_pipeline(
        question=request.question,
        top_k=request.top_k
    )

    return result