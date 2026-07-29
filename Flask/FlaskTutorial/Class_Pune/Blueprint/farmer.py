from flask import Blueprint, jsonify

farmer_bp=Blueprint('farmer',__name__)

@farmer_bp.route('/farmer')
def farmer():
    return jsonify({'message':'Farmer Page'})       


@farmer_bp.route('/info')
def farmer_info():    
    return jsonify({'message':'Farmer Info Page'})  
