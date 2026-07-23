from flask import Flask, request, session, redirect
from middleware import auth

app = Flask(__name__)
app.secret_key = "12345"

@app.route("/")
def home():
    return """
    <h2>Home Page</h2>
    <a href="/login">Login</a>
    """

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        session["email"] = email
        return redirect("/dashboard")

    return """
    <h2>Login</h2>
    <form method="POST">
        <input type="email" name="email" placeholder="Enter Email">
        <button type="submit">Login</button>
    </form>
    """

@app.route("/dashboard")
@auth
def dashboard():
    return f"""
    <h2>Dashboard</h2>
    <p>Welcome {session['email']}</p>
    <a href="/logout">Logout</a>
    """

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
