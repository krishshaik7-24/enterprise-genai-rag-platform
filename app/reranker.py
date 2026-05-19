def rerank_results(results):
    """
    Re-ranks retrieved chunks based on FAISS distance.

    Lower distance means the chunk is more relevant.
    """
    sorted_results = sorted(results, key=lambda item: item["distance"])

    reranked_results = []

    for new_rank, result in enumerate(sorted_results, start=1):
        reranked_results.append(
            {
                "rank": new_rank,
                "source": result["source"],
                "chunk_id": result["chunk_id"],
                "text": result["text"],
                "distance": result["distance"]
            }
        )

    return reranked_results