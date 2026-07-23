import { useState, useEffect } from 'react';
// import axios from 'axios';
import api from './api';

function App() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    // Calling the API using our clean separate instance
    api.get('') // This automatically targets http://localhost:5000/api/data
      .then(response => {
        setMessage(response.data.message); 
      })
      .catch(error => {
        console.error("Error fetching data:", error);
        setMessage("Could not connect to the backend server!");
      });
  }, []);


  return (
    <div style={{ textAlign: 'center', marginTop: '50px', fontFamily: 'Arial, sans-serif' }}>
      <h1>React + Flask Connection</h1>
      <p>Message from backend: <strong>{message}</strong></p>
    </div>
  );
}

export default App;
