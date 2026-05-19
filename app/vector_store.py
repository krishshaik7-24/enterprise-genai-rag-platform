import faiss
import numpy as np

from app.embeddings import create_embeddings


class VectorStore:
    def __init__(self):
        self.index = None
        self.chunks = []
        self.dimension = None

    def build_index(self, chunks):
        """
        Builds a FAISS index from document chunks.
        """
        self.chunks = chunks
        texts = [chunk["text"] for chunk in chunks]

        embeddings = create_embeddings(texts)
        embeddings = embeddings.astype("float32")

        self.dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(embeddings)

        return {
            "status": "success",
            "total_chunks_indexed": len(chunks),
            "embedding_dimension": self.dimension
        }

    def search(self, query: str, top_k: int = 3):
        """
        Searches FAISS for the most relevant chunks.
        """
        if self.index is None:
            raise ValueError("Vector index has not been built yet. Please run ingestion first.")

        query_embedding = create_embeddings([query])
        query_embedding = query_embedding.astype("float32")

        distances, indices = self.index.search(query_embedding, top_k)

        results = []

        for rank, chunk_index in enumerate(indices[0]):
            if chunk_index == -1:
                continue

            chunk = self.chunks[chunk_index]

            results.append(
                {
                    "rank": rank + 1,
                    "source": chunk["source"],
                    "chunk_id": chunk["chunk_id"],
                    "text": chunk["text"],
                    "distance": float(distances[0][rank])
                }
            )

        return results