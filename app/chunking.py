def split_documents_into_chunks(documents, chunk_size: int = 500, chunk_overlap: int = 100):
    """
    Splits document content into smaller chunks.

    Args:
        documents: List of dictionaries with source and content.
        chunk_size: Maximum number of characters in each chunk.
        chunk_overlap: Number of overlapping characters between chunks.

    Returns:
        A list of chunk dictionaries.
    """
    chunks = []

    for document in documents:
        source = document["source"]
        content = document["content"]

        start = 0
        chunk_number = 1

        while start < len(content):
            end = start + chunk_size
            chunk_text = content[start:end]

            chunks.append(
                {
                    "source": source,
                    "chunk_id": f"{source}_chunk_{chunk_number}",
                    "text": chunk_text
                }
            )

            chunk_number += 1
            start += chunk_size - chunk_overlap

    return chunks