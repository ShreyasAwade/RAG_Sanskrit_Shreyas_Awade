Frontend - 

# 🧠 Sanskrit RAG Frontend (React UI)

## 📌 Overview

This is the frontend interface for the Sanskrit Retrieval-Augmented Generation (RAG) system. It provides a clean and interactive UI for users to:

* Upload Sanskrit documents (.txt / .pdf)
* Ask questions in Sanskrit (or transliterated text)
* View generated answers based on retrieved context

The frontend communicates with a Flask-based backend via REST APIs.

---

## 🚀 Features

* 📄 File upload support (.txt, .pdf)
* 💬 Chat-style question-answer interface
* ⚡ Real-time API interaction
* 🔒 Input validation (prevents querying before upload)
* 📱 Responsive UI (works on desktop and mobile)
* 🎨 Clean and modern design using Bootstrap + custom CSS

---

## 🛠️ Tech Stack

* **React.js** – UI development
* **Bootstrap** – Styling and responsiveness
* **Axios** – API communication
* **JavaScript (ES6+)**

---

## 📂 Project Structure

```
frontend/
│
├── src/
│   ├── App.js
│   ├── App.css
│   ├── index.js
│   │
│   ├── services/
│   │   └── api.js
│
├── public/
├── package.json
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-url>
cd frontend
```

### 2. Install dependencies

```
npm install
```

### 3. Start the development server

```
npm start
```

The app will run on:

```
http://localhost:3000
```

---

## 🔗 Backend Integration

Ensure the backend server is running at:

```
http://127.0.0.1:5000
```

Update API base URL in:

```
src/services/api.js
```

---

## 📡 API Endpoints Used

### 1. Upload Document

```
POST /upload
```

* Sends file using FormData
* Builds retrieval index on backend

---

### 2. Query

```
POST /query
```

Request:

```
{
  "query": "धर्मः किम्?"
}
```

Response:

```
{
  "answer": "..."
}
```

---

## 🧠 Usage Flow

1. Upload a Sanskrit document
2. Wait for successful processing
3. Enter a query
4. View generated answer in chat interface

---

## ⚠️ Notes & Limitations

* Only one document is active at a time
* Uploading a new file replaces the previous context
* Requires backend to be running
* Model performance depends on document quality and query clarity

---

## 💡 Future Improvements

* Chat history persistence
* Multi-document support
* Typing animation for responses
* File upload progress indicator
* User session handling

---

## 👨‍💻 Author

Shreyas Awade

---

Backend - 

# 🧠 Sanskrit RAG Backend (Flask API)

## 📌 Overview

This backend implements a **Retrieval-Augmented Generation (RAG)** pipeline for Sanskrit documents. It allows users to upload documents and query them using natural language. The system retrieves relevant context and generates answers using a CPU-based LLM.

---

## ⚙️ System Architecture

```id="j3p4ts"
User Input
   ↓
Flask API (/upload, /query)
   ↓
Preprocessing → Chunking
   ↓
Embeddings (Sentence Transformers)
   ↓
FAISS Vector Store
   ↓
Retriever (Top-K search)
   ↓
LLM (FLAN-T5)
   ↓
Generated Answer
```

---

## 🚀 Features

* 📄 Dynamic document upload (.txt, .pdf)
* ⚡ In-memory processing (no file storage required)
* 🔍 Semantic search using vector embeddings
* 🤖 Answer generation using CPU-based LLM
* 🔗 REST API endpoints for integration
* 🧩 Modular pipeline (loader, preprocess, retriever, generator)

---

## 🛠️ Tech Stack

* **Flask** – API framework
* **Sentence Transformers** – Text embeddings
* **FAISS** – Vector similarity search
* **Transformers (FLAN-T5)** – Text generation
* **PyMuPDF** – PDF parsing
* **NumPy** – Numerical operations

---

## 📂 Project Structure

```id="66bb9x"
backend/
│
├── app.py              # Main API server
├── loader.py           # File loading (TXT, PDF)
├── preprocess.py       # Cleaning + chunking
├── embedder.py         # Embedding model
├── retriever.py        # FAISS-based retrieval
├── generator.py        # LLM response generation
├── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Navigate to backend

```id="t9bjti"
cd backend
```

### 2. Install dependencies

```id="2zplqg"
pip install -r requirements.txt
```

### 3. Run the server

```id="9dnv2c"
python app.py
```

Server runs on:

```id="x7hl6c"
http://127.0.0.1:5000
```

---

## 📡 API Endpoints

### 1. Health Check

```id="c1pn9j"
GET /
```

Response:

```id="cvn1rh"
Sanskrit RAG API is running 🚀
```

---

### 2. Upload Document

```id="3qmvz8"
POST /upload
```

* Accepts: `.txt`, `.pdf`
* Input: `multipart/form-data`

Response:

```id="tv6yrh"
{
  "message": "File uploaded and processed successfully",
  "chunks": 12
}
```

---

### 3. Query

```id="l6s49s"
POST /query
```

Request:

```id="cs1qwy"
{
  "query": "धर्मः किम्?"
}
```

Response:

```id="z3hy0y"
{
  "query": "धर्मः किम्?",
  "answer": "..."
}
```

---

## 🧠 Processing Pipeline

### 1. Document Ingestion

* File uploaded via API
* Processed in-memory (no disk storage)

### 2. Preprocessing

* Text normalization
* Removal of extra whitespace

### 3. Chunking

* Splits text into overlapping segments
* Improves retrieval accuracy

### 4. Embedding

* Uses SentenceTransformer model
* Converts text into vector representations

### 5. Retrieval

* FAISS performs similarity search
* Top-K relevant chunks selected

### 6. Generation

* FLAN-T5 generates response using retrieved context

---

## ⚠️ Limitations

* Single document at a time (new upload replaces previous)
* CPU-based inference → slower response time
* Limited Sanskrit understanding of general-purpose models
* No persistent storage (index resets on restart)

---

## 💡 Future Improvements

* Multi-document support
* Persistent FAISS index
* User session-based retrieval
* Improved Sanskrit-specific models
* Performance optimization for CPU

---

## 👨‍💻 Author

Shreyas Awade

---


