from flask import Flask
import threading  
import sys

app = Flask(__name__)

# Check terminal inputs safely
if len(sys.argv) > 1:
    PORT_NUMBER = int(sys.argv[1]) # Reads the correct index
else:
    PORT_NUMBER = 5000 # Default fallback port

@app.route('/')
def home():
    current_thread = threading.current_thread().name
    return f"Response from Thread: {current_thread} on Port: {PORT_NUMBER}"

if __name__ == '__main__':
    print(f"Starting server on port {PORT_NUMBER}...")
    app.run(debug=True, use_reloader=False, port=PORT_NUMBER)
