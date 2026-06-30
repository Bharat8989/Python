from flask import Blueprint

product_bp=Blueprint('product',__name__,url_prefix='/user')

@product_bp.route('/product')
def product():
    return "this is product page "