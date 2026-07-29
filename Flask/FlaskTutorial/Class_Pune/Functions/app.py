from flask import Flask,request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Flask Calculator App! Use  /add/10/15,  /sub/10/5, or    /mult/10/5 in the URL.'

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    result = num1 + num2
    return f'The addition of {num1} and {num2} is: {result}'


@app.route('/sub/<int:num1>/<int:num2>')
def sub(num1, num2):
    result = num1 - num2
    return f'The subtraction of {num1} and {num2} is: {result}'


@app.route('/mult/<int:num1>/<int:num2>')
def mult(num1, num2):
    result = num1 * num2
    return f'The multiplication of {num1} and {num2} is: {result}'

@app.route('/additions', methods=['POST', 'GET'])
def additions():


    if request.method == 'POST':
        data = request.get_json()
        num1 = data.get('num1', 0)
        num2 = data.get('num2', 0)
        result = num1 + num2
        
        return jsonify({
            "message": "Addition successful (via POST)",
            "num1": num1,
            "num2": num2,
            "result": result
        })

    num1 = int(request.args.get('num1', default=0))
    num2 = int(request.args.get('num2', default=0))
    result = num1 + num2
    
    return jsonify({
        "message": "Showing data via GET",
        "num1": num1,
        "num2": num2,
        "result": result
    })

if __name__ == '__main__':
    app.run(debug=True)