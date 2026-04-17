import React, { useState } from "react";
import { uploadFile, sendQuery } from "./services/api";
import "./App.css";

function App() {
    const [file, setFile] = useState(null);
    const [uploaded, setUploaded] = useState(false);
    const [messages, setMessages] = useState([]);
    const [query, setQuery] = useState("");
    const [loading, setLoading] = useState(false);

    // Upload file
    const handleUpload = async () => {
        if (!file) return alert("Select a file");

        setLoading(true);
        const res = await uploadFile(file);
        setLoading(false);

        if (res.error) {
            alert(res.error);
        } else {
            setUploaded(true);
            alert("Document uploaded successfully");
        }
    };

    // Send query
    const handleSend = async () => {
        if (!query.trim()) return;

        const userMsg = { text: query, sender: "user" };
        setMessages((prev) => [...prev, userMsg]);

        setQuery("");
        setLoading(true);

        const res = await sendQuery(query);

        setLoading(false);

        const botMsg = {
            text: res.answer || res.error,
            sender: "bot"
        };

        setMessages((prev) => [...prev, botMsg]);
    };

    return (
        <div className="app-container">

            <div className="chat-wrapper">

                <h3 className="title">🧠 Sanskrit RAG Assistant</h3>

                {/* Upload Section */}
                <div className="upload-box">
                    <input
                        type="file"
                        onChange={(e) => setFile(e.target.files[0])}
                    />
                    <button onClick={handleUpload}>
                        Upload
                    </button>
                </div>

                {/* Chat Box */}
                <div className="chat-box">

                    {messages.map((msg, i) => (
                        <div
                            key={i}
                            className={`message ${msg.sender}`}
                        >
                            {msg.text}
                        </div>
                    ))}

                    {loading && <div className="message bot">Thinking...</div>}
                </div>

                {/* Input */}
                <div className="input-box">
                    <input
                        type="text"
                        placeholder="Ask in Sanskrit..."
                        value={query}
                        onChange={(e) => setQuery(e.target.value)}
                        disabled={!uploaded}
                    />
                    <button onClick={handleSend} disabled={!uploaded}>
                        Send
                    </button>
                </div>

            </div>
        </div>
    );
}

export default App;