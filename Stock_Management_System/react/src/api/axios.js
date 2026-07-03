import axios from "axios";

const api = axios.create({
    // Point this to the root of your backend server, not a specific route
    baseURL: "http://127.0.0.1:5000", 
    headers: {
        "Content-Type": "application/json",
    },
    timeout: 10000,
});

export default api;
