import faiss
import numpy as np

class Retriever:
    def __init__(self, embeddings, chunks):
        self.chunks = chunks
        self.index = faiss.IndexFlatL2(384)
        self.index.add(np.array(embeddings))

    def search(self, query_embedding, k=3):
        D, I = self.index.search(np.array([query_embedding]), k)
        return [self.chunks[i] for i in I[0]]