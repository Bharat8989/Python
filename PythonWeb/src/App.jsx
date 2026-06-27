// src/App.jsx
import { useState } from 'react';

function App() {
  // Simple state to show static text
  const [message, setMessage] = useState('Welcome to React!');

  return (
    <div style={{ textAlign: 'center', marginTop: '50px', fontFamily: 'sans-serif' }}>
      <h1>Home Page</h1>
      <h2>Frontend Status: {message}</h2>
      
      {/* Click the button to test local state changing without any server */}
      <button 
        onClick={() => setMessage('React is running beautifully offline!')}
        style={{ padding: '10px 20px', fontSize: '16px', cursor: 'pointer', backgroundColor: '#646cff', color: 'white', border: 'none', borderRadius: '4px' }}
      >
        Click Me
      </button>
    </div>
  );
}

export default App;
