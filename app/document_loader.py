from pathlib import Path


def load_text_documents(data_folder: str = "data"):
    """
    Loads all .txt files from the data folder.

    Returns:
        A list of dictionaries. Each dictionary contains:
        - source: file name
        - content: file text
    """
    documents = []
    folder_path = Path(data_folder)

    if not folder_path.exists():
        raise FileNotFoundError(f"Data folder not found: {data_folder}")

    for file_path in folder_path.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        documents.append(
            {
                "source": file_path.name,
                "content": text
            }
        )

    return documents