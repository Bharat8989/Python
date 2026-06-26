# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 

@app.route('/api/data', methods=['GET'])
def get_data():
    # You must wrap your text in jsonify() like this:
    return jsonify({"message": "hello world"})

@app.route('/api/send', methods=['POST'])
def receive_data():
    return jsonify({"message": "hello bharat"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
