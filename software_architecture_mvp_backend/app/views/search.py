from flask import Blueprint, request, jsonify
from app import db
from app.models import Product, Store

search_bp = Blueprint('search_bp', __name__)

@search_bp.route('/search/products', methods=['GET'])
def search_products():
    query = request.args.get('q', '')

    products = Product.query.filter(Product.name.ilike(f'%{query}%')).all()
    result = [{'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price, 'store_id': product.store_id} for product in products]

    return jsonify(result), 200

@search_bp.route('/search/stores', methods=['GET'])
def search_stores():
    query = request.args.get('q', '')

    stores = Store.query.filter(Store.name.ilike(f'%{query}%')).all()
    result = [{'id': store.id, 'name': store.name, 'owner_id': store.owner_id} for store in stores]

    return jsonify(result), 200

