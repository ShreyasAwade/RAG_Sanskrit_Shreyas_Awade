import axios from "axios";

const BASE_URL = "http://127.0.0.1:5000";

// Upload file
export const uploadFile = async (file) => {
    const formData = new FormData();
    formData.append("file", file);

    try {
        const res = await axios.post(`${BASE_URL}/upload`, formData);
        return res.data;
    } catch (err) {
        return { error: "Upload failed" };
    }
};

// Send query
export const sendQuery = async (query) => {
    try {
        const res = await axios.post(`${BASE_URL}/query`, { query });
        return res.data;
    } catch (err) {
        return { error: "Query failed" };
    }
};