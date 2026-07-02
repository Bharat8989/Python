from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    name='bharat'
    age=34
    email='bharat@gmail.com'

    return render_template('app.html',name=name,age=age,email=email)



@app.route('/contact')
def contact():
    return 'contact us page'

if __name__ == '__main__':
    app.run(debug=True)

