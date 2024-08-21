from flask import Blueprint, request, jsonify
from app import db
from app.models import Product

product_bp = Blueprint('product_bp', __name__)

# Route to get products by store_id
@product_bp.route('/views/products', methods=['GET'])
def get_products():
    store_id = request.args.get('store_id')
    if not store_id:
        return jsonify({'error': 'store_id is required'}), 400

    products = Product.query.filter_by(store_id=store_id).all()
    return jsonify([product.to_dict() for product in products])

# Route to create a new product
@product_bp.route('/views/products', methods=['POST'])
def create_product():
    data = request.json
    if 'store_id' not in data:
        return jsonify({'error': 'store_id is required'}), 400

    try:
        price = float(data['price'])
        formatted_price = f"{price:.2f}"
    except ValueError:
        return jsonify({'error': 'Invalid price format'}), 400

    new_product = Product(
        store_id=data['store_id'],
        name=data['name'],
        description=data['description'],
        price=formatted_price,
        unit=data.get('unit') 
    )
    db.session.add(new_product)
    db.session.commit()

    return jsonify({'message': 'Product created successfully', 'product': new_product.to_dict()}), 201

# Route to update an existing product
@product_bp.route('/views/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    product = Product.query.get(id)

    if not product:
        return jsonify({'error': 'Product not found'}), 404

    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    if 'price' in data:
        try:
            price = float(data['price'])
            product.price = f"{price:.2f}"
        except ValueError:
            return jsonify({'error': 'Invalid price format'}), 400
    product.unit = data.get('unit', product.unit) 

    db.session.commit()
    return jsonify(product.to_dict())

# Route to delete a product
@product_bp.route('/views/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)

    if not product:
        return jsonify({'error': 'Product not found'}), 404

    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})