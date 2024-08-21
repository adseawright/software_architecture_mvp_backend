from flask import Blueprint, request, jsonify
from app import db
from app.models import User
import bcrypt
import jwt
import datetime
import os

# Blueprint for the login routes
login_bp = Blueprint('login', __name__)

# Define the login route
@login_bp.route('/login', methods=['POST'])
def login():
    # Get the data from the request
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Check if email or password is missing
    if not email or not password:
        return jsonify({'message': 'Missing data'}), 400

    # Query the database for the user
    user = User.query.filter_by(email=email).first()

    # Verify the password
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        # Generate a JWT token valid for 24 hours
        token = jwt.encode({'user_id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, os.getenv('SECRET_KEY'), algorithm='HS256')
        return jsonify({'token': token, 'user_id': user.id}), 200
    else:
        # Return an error if the credentials are invalid
        return jsonify({'message': 'Invalid credentials'}), 401