from flask import Flask, request

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        return f"Welcome {username}"

    return '''
        <form method="POST">
            <input type="text" name="username">
            <input type="submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask, request

# app = Flask(__name__)

# @app.route("/login", methods=["GET", "POST"])
# def login():

#     if request.args.get == "GET":
#         username = request.args.get["username"]
#         return f"Welcome {username}"

#     return '''
#         <form method="GET">
#             <input type="text" name="username">
#             <input type="submit">
#         </form>
#     '''

# if __name__ == "__main__":
#     app.run(debug=True)