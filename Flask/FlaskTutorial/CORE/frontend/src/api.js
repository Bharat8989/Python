import axios from 'axios';

// Create an instance of axios with a base URL
const api = axios.create({
  baseURL: 'http://localhost:5000/api', // automatically adds this to all requests
  timeout: 5000, // drops request if server takes more than 5 seconds
  headers: {
    'Content-Type': 'application/json'
  }
});

export default api;
