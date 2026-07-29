from flask import Flask
from farmer import farmer_bp
from admin import admin_bp


app=Flask(__name__)

app.register_blueprint(farmer_bp, url_prefix='/farmer_up')
app.register_blueprint(admin_bp, url_prefix='/farmer_down')

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)