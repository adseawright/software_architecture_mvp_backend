from flask import Blueprint, request, jsonify
from app import db
from app.models import User
import bcrypt
import jwt
import datetime

# Create a Blueprint for the register endpoint
register_bp = Blueprint('register', __name__)

# Define the register endpoint
@register_bp.route('/register', methods=['POST'])
def register():
    # Get the data from the request
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    # Check if any required data is missing
    if not email or not username or not password:
        return jsonify({'message': 'Missing data'}), 400

    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    # Create a new User object
    new_user = User(email=email, username=username, password=hashed_password)
    
    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    # Generate a JWT token for the new user
    token = jwt.encode({'user_id': new_user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, 'your_secret_key', algorithm='HS256')
    # Return the token and user_id to the client
    return jsonify({'token': token, 'user_id': new_user.id}), 201