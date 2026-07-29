from flask import Blueprint, jsonify

admin_bp=Blueprint('admin',__name__)

@admin_bp.route('/admin')
def admin():
    return jsonify({'message':'Admin Page'})