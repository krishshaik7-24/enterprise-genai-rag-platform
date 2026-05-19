from app.retriever import retrieve_relevant_chunks
from app.reranker import rerank_results


def generate_answer_from_context(question: str, context_chunks):
    """
    Creates a simple answer using the retrieved context.
    This is a lightweight local response generator for project demonstration.
    """
    if not context_chunks:
        return "I could not find relevant information in the available documents."

    combined_context = " ".join([chunk["text"] for chunk in context_chunks])

    answer = (
        "Based on the available enterprise documents, the most relevant information is: "
        + combined_context[:700]
    )

    return answer


def run_rag_pipeline(question: str, top_k: int = 3):
    """
    Runs the full RAG workflow:
    1. Retrieve relevant chunks
    2. Re-rank chunks
    3. Generate answer from context
    """
    retrieved_chunks = retrieve_relevant_chunks(question, top_k=top_k)
    reranked_chunks = rerank_results(retrieved_chunks)

    answer = generate_answer_from_context(question, reranked_chunks)

    sources = list({chunk["source"] for chunk in reranked_chunks})

    return {
        "question": question,
        "answer": answer,
        "sources": sources,
        "retrieved_chunks": reranked_chunks
    }