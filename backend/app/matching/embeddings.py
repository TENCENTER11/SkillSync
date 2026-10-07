from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    """
    Generates semantic embeddings for skills,
    job descriptions, and career profiles.
    """

    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def encode(self, text: str):
        """
        Convert text into a semantic vector.
        """

        return self.model.encode(
            text,
            normalize_embeddings=True
        )

    def encode_multiple(self, texts: list[str]):
        """
        Convert multiple texts into semantic vectors.
        """

        return self.model.encode(
            texts,
            normalize_embeddings=True
        )


embedding_model = EmbeddingModel()