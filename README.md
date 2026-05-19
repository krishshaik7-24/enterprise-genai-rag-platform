# Enterprise GenAI RAG Platform

A semantic document retrieval and Retrieval-Augmented Generation platform built using FastAPI, FAISS, and Python. This project demonstrates how enterprise users can search financial and policy documents using AI-powered semantic search.

## Project Overview

This platform allows users to ask natural language questions about enterprise documents. The system loads documents, splits them into chunks, creates embeddings, stores them in a FAISS vector index, retrieves the most relevant chunks, re-ranks results, and returns an answer with source references.

## Features

- Semantic document retrieval
- FastAPI backend
- FAISS vector search
- Sentence Transformer embeddings
- Document chunking pipeline
- Simple re-ranking logic
- RAG-style answer generation
- Swagger API documentation
- GitHub-ready project structure

## Tech Stack

- Python
- FastAPI
- FAISS
- Sentence Transformers
- Pydantic
- Uvicorn
- Git and GitHub
- Docker

## Project Structure

```text
enterprise-genai-rag-platform/
│
├── app/
│   ├── main.py
│   ├── document_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── reranker.py
│   └── rag_pipeline.py
│
├── data/
│   ├── sample_financial_report.txt
│   └── sample_policy_document.txt
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── project_report.md
├── .env.example
└── .gitignore