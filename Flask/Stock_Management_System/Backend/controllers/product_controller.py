# Backend/controllers/product_controller.py
from flask import jsonify, request # pyright: ignore[reportMissingImports]
from config.db_config import get_db_connection

def get_all_products():
    db = get_db_connection()
    if db is None:
        return jsonify({"error": "Database connection failed"}), 500
        
    cursor = db.cursor(dictionary=True) 
    try:
        cursor.execute("SELECT * FROM products ORDER BY id DESC")
        products = cursor.fetchall()
        return jsonify(products), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        db.close()

def add_new_product():
    data = request.json
    if not data or 'name' not in data or 'stock' not in data or 'price' not in data:
        return jsonify({"error": "Missing required fields (name, stock, price)"}), 400

    db = get_db_connection()
    if db is None:
        return jsonify({"error": "Database connection failed"}), 500
        
    cursor = db.cursor()
    try:
        query = "INSERT INTO products (name, stock, price) VALUES (%s, %s, %s)"
        values = (data['name'], int(data['stock']), float(data['price']))
        cursor.execute(query, values)
        db.commit()
        return jsonify({"message": "Product added successfully!", "id": cursor.lastrowid}), 201
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        db.close()

def update_product(product_id):
    data = request.json
    db = get_db_connection()
    if db is None:
        return jsonify({"error": "Database connection failed"}), 500
        
    cursor = db.cursor()
    try:
        query = "UPDATE products SET name = %s, stock = %s, price = %s WHERE id = %s"
        values = (data['name'], int(data['stock']), float(data['price']), product_id)
        cursor.execute(query, values)
        db.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Product not found"}), 404
        return jsonify({"message": "Product updated successfully!"}), 200
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        db.close()

def delete_product(product_id):
    db = get_db_connection()
    if db is None:
        return jsonify({"error": "Database connection failed"}), 500
        
    cursor = db.cursor()
    try:
        query = "DELETE FROM products WHERE id = %s"
        cursor.execute(query, (product_id,))
        db.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Product not found"}), 404
        return jsonify({"message": "Product deleted successfully!"}), 200
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        db.close()
