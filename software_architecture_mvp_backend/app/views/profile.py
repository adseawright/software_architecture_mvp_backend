from flask import Blueprint, request, jsonify
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError
from app import db
from app.models import User

profile_bp = Blueprint('profile_bp', __name__)
CORS(profile_bp)  # Enable CORS for the Blueprint

# Route to get the profile of a user by user_id
@profile_bp.route('/profile', methods=['GET'])
def get_profile():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({
        'username': user.username,
        'email': user.email
    })

# Route to update the profile of a user by user_id
@profile_bp.route('/profile/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
    data = request.json
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    if 'password' in data:
        user.password = data['password'] 

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email already exists'}), 400

    return jsonify({'message': 'Profile updated successfully', 'profile': user.to_dict()})

# Route to delete the profile of a user by user_id
@profile_bp.route('/profile/<int:user_id>', methods=['DELETE'])
def delete_profile(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'Profile deleted successfully'})