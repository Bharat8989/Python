from flask import Flask, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app,origins=['http://localhost:5173'])  

@app.route('/api', methods=['GET'])
def get_data():
    
    return jsonify({"message": "Hello from Flask Backend!", "status": "success"})

@app.route('/data',methods=['GET'])
def get_show():
    data=['hello',23,'pavan']
    return jsonify(data)




if __name__ == '__main__':
    app.run(debug=True ,port=5000)  