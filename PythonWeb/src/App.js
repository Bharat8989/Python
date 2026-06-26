import React, { useState, useEffect } from 'react';
// import logo from './logo.svg';
// import './App.css';

function App() {
  const [backendMessage, setBackendMessage] = useState('Loading...');

  useEffect(() => {
    fetch('http://localhost:5000/api/data')
      .then((res) => res.json()) // Looks for the JSON object
      .then((data) => {
        setBackendMessage(data.message); // Extracts 'hello world'
      })
      .catch((err) => {
        console.error("Error:", err);
        setBackendMessage('Server Error!');
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        
        {/* This will now display: hello world */}
        <h1 style={{ color: '#61dafb' }}>{backendMessage}</h1>
        
        <p>Data successfully received from app.py!</p>
      </header>
    </div>
  );
}

export default App;
