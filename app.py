# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS

from loader import load_txt, load_pdf
from preprocess import clean_text, chunk_text
from embedder import get_embeddings, model
from retriever import Retriever
from generator import generate_answer

# -------------------------------
# INIT APP
# -------------------------------
app = Flask(__name__)
CORS(app)

# Global retriever
retriever = None


# -------------------------------
# ROOT ROUTE
# -------------------------------
@app.route("/")
def home():
    return "Sanskrit RAG API is running"


# -------------------------------
# HEALTH CHECK
# -------------------------------
@app.route("/health")
def health():
    return {"status": "ok"}


# -------------------------------
# FILE UPLOAD
# -------------------------------
@app.route("/upload", methods=["POST"])
def upload():
    global retriever

    # Check file presence
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    # Validate filename
    if file.filename.strip() == "":
        return jsonify({"error": "Invalid file name"}), 400

    try:
        filename = file.filename.lower()

        # -------------------------------
        # LOAD FILE (IMPORTANT: read once)
        # -------------------------------
        if filename.endswith(".pdf"):
            text = load_pdf(file)
        elif filename.endswith(".txt"):
            text = load_txt(file)
        else:
            return jsonify({"error": "Only .txt or .pdf supported"}), 400

        # Validate extracted text
        if not text or len(text.strip()) == 0:
            return jsonify({"error": "File is empty or unreadable"}), 400

        # -------------------------------
        # PREPROCESS
        # -------------------------------
        text = clean_text(text)

        # -------------------------------
        # CHUNKING
        # -------------------------------
        chunks = chunk_text(text)

        if len(chunks) == 0:
            return jsonify({"error": "Chunking failed"}), 500

        # -------------------------------
        # EMBEDDINGS
        # -------------------------------
        embeddings = get_embeddings(chunks)

        # -------------------------------
        # BUILD RETRIEVER
        # -------------------------------
        retriever = Retriever(embeddings, chunks)

        return jsonify({
            "message": "File uploaded and processed successfully",
            "chunks": len(chunks)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -------------------------------
# QUERY
# -------------------------------
@app.route("/query", methods=["POST"])
def query():
    global retriever

    # Ensure upload happened
    if retriever is None:
        return jsonify({"error": "Upload document first"}), 400

    data = request.json

    if not data or "query" not in data:
        return jsonify({"error": "Invalid request"}), 400

    user_query = data["query"].strip()

    if user_query == "":
        return jsonify({"error": "Empty query"}), 400

    try:
        # -------------------------------
        # EMBED QUERY
        # -------------------------------
        query_embedding = model.encode(user_query)

        # -------------------------------
        # RETRIEVE CONTEXT
        # -------------------------------
        retrieved_chunks = retriever.search(query_embedding)

        if not retrieved_chunks:
            return jsonify({"error": "No relevant context found"}), 500

        context = " ".join(retrieved_chunks)

        # -------------------------------
        # GENERATE ANSWER
        # -------------------------------
        answer = generate_answer(user_query, context)

        return jsonify({
            "query": user_query,
            "answer": answer
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -------------------------------
# RUN SERVER
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)