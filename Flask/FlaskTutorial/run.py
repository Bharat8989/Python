from flask import Flask,jsonify,request

app=Flask(__name__)

data=[
    {
        "id":1,
        "name":"Bharat",
        "age":23
    }
]

@app.route('/')
def home():
    return "this is home page"

@app.route('/user',methods=['GET'])
def user():
    # return str(data)
    return jsonify(data)


# add the put method add the new data

@app.route('/user',methods=['POST'])

def add_user():
    request_data=request.get_json() or {}
    
    new_user={
        "id":request_data.get["id"],
        "name":request_data.get["name"],
        "age":request_data.get["age"],
        
    }
    data.append(new_user)
    # print(data)
    # return str(data)
    return jsonify(new_user), 201

if __name__=='__main__':
    app.run(debug=True)