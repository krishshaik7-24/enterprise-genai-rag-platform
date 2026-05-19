from sentence_transformers import SentenceTransformer


_model = None


def get_embedding_model():
    """
    Loads the sentence transformer embedding model only once.
    """
    global _model

    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")

    return _model


def create_embeddings(texts):
    """
    Converts a list of text values into embeddings.

    Args:
        texts: List of text strings.

    Returns:
        Embeddings as a numpy array.
    """
    model = get_embedding_model()
    embeddings = model.encode(texts, convert_to_numpy=True)

    return embeddings