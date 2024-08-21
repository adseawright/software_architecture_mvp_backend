from flask import Blueprint, request, jsonify
from app import db
from app.models import Store

# Create a Blueprint for the store endpoints
store_bp = Blueprint('store_bp', __name__)

# Endpoint to get all stores for a specific owner
@store_bp.route('/views/stores', methods=['GET'])
def get_stores():
    # Get the owner ID from the request parameters
    owner_id = request.args.get('owner_id')
    if not owner_id:
        return jsonify({'error': 'Owner ID is required'}), 400

    # Query the database for stores belonging to the owner
    stores = Store.query.filter_by(owner_id=owner_id).all()
    # Return the stores as JSON
    return jsonify([store.to_dict() for store in stores])

# Endpoint to create a new store
@store_bp.route('/views/stores', methods=['POST'])
def create_store():
    # Get the data from the request body
    data = request.json
    # Create a new store object
    new_store = Store(
        name=data['name'],
        description=data.get('description', ''),  # Use empty string if description is not provided
        owner_id=data['owner_id']
    )
    # Add and commit the new store to the database
    db.session.add(new_store)
    db.session.commit()

    # Return a success message and the new store as JSON
    return jsonify({'message': 'Store created successfully', 'store': new_store.to_dict()}), 201

# Endpoint to update an existing store
@store_bp.route('/views/stores/<int:store_id>', methods=['PUT'])
def update_store(store_id):
    # Get the data from the request body
    data = request.json
    # Query the database for the store to update
    store = Store.query.get(store_id)
    if not store:
        return jsonify({'error': 'Store not found'}), 404

    # Update the store's name and description
    store.name = data.get('name', store.name)
    store.description = data.get('description', store.description)
    # Commit the changes to the database
    db.session.commit()

    # Return a success message and the updated store as JSON
    return jsonify({'message': 'Store updated successfully', 'store': store.to_dict()})

# Endpoint to delete an existing store
@store_bp.route('/views/stores/<int:store_id>', methods=['DELETE'])
def delete_store(store_id):
    # Query the database for the store to delete
    store = Store.query.get(store_id)
    if not store:
        return jsonify({'error': 'Store not found'}), 404

    # Delete the store from the database
    db.session.delete(store)
    db.session.commit()

    # Return a success message
    return jsonify({'message': 'Store deleted successfully'})