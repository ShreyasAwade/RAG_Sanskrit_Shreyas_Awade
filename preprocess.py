#Text Cleaning
def clean_text(text):
    text = text.replace("\n", " ")
    text = " ".join(text.split())
    return text

#Split text into the chunks
def chunk_text(text, chunk_size=400, overlap=50):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))
    return chunks