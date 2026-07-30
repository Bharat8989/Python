# from flask import Flask,request

# app=Flask(__name__)

# @app.route('/',methods=['POST'])
# def login():
#     # total=0
#     # interest=0
    
#     if request.method=='POST':
#         name=str(request.form.get('name',))
#         email=str(request.form.get('email'))
#         age=int(request.form.get('age'))

        
        
#     return f' name:{name}, email:{email},age:{age}'
        
        
# if __name__=='__main__':
#     app.run(debug=True)


from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def login():
    if request.method == 'POST':
        # request.get_json() parses the incoming JSON data into a Python dictionary
        data = request.get_json() or {}
        
        name = str(data.get('name'))
        email = str(data.get('email'))
        age = int(data.get('age'))
        
        response_data = {
            
            "user": {
                "name": name,
                "email": email,
                "age": age
            }
        }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
