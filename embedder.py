from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

#convert text list into embeddings
def get_embeddings(text_list):
    return model.encode(text_list)
