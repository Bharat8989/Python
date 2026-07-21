from flask import Flask
import logging

app = Flask(__name__)

# 1. Configuration Settings (FIXED: Named correctly and removed trailing comma)
log_level = logging.DEBUG
log_file = 'app.log'
log_file_mode = 'a'
log_format = '%(asctime)s - %(levelname)s - %(message)s'

# 2. Initialize the logging engine with your configurations
logging.basicConfig(
    level=log_level, 
    filename=log_file, 
    filemode=log_file_mode,
    format=log_format
)

@app.route('/')
def index():
    # 3. Writing logs when this route is visited
    logging.debug("The index route function was triggered successfully.")
    logging.info("Hello World page served to the user.")
    return 'hello world !!'

@app.route('/user')
def user():
    logging.debug('this debug for the user route')
    return 'hello user '

if __name__ == '__main__':
    app.run(debug=True)
