from flask import Flask ,request ,jsonify
from flask_cors import CORS
app=Flask(__name__)
 
CORS(app)
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if data['email']=='admin@gmail.com' and data['password']=='1234':
        
        return jsonify({
            'status':True,
            'token':'JWT_TOKEN_ABC123'
        })
    return jsonify({
        'status':False,
        'message':'invalid credentials'

    })
if __name__=='__main__':
    app.run(debug=True)