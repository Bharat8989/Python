# Backend/app.py
from flask import Flask # pyright: ignore[reportMissingImports]
from flask_cors import CORS
from config.db_config import init_db
from controllers.product_controller import get_all_products, add_new_product, update_product, delete_product

app = Flask(__name__)
# Explicitly allowing your frontend to communicate with your backend APIs
CORS(app)

# Automatically verifies and builds database schemas on start
init_db()

@app.route('/')
def home():
    return "this is home page "

@app.route('/api/products', methods=['GET'])
def get_items(): 
    return get_all_products()

@app.route('/api/products', methods=['POST'])
def add_item(): 
    return add_new_product()

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def edit_item(product_id): 
    return update_product(product_id)

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def remove_item(product_id): 
    return delete_product(product_id)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
