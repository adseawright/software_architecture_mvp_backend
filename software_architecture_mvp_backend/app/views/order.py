from flask import Blueprint, request, jsonify
import requests
import os
import traceback  # Import traceback for detailed error logging
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()

# Blueprint for orders
order_bp = Blueprint('order_bp', __name__)

class PayPalClient:
    def __init__(self):
        self.access_token = None
        self.token_expiry = 0  # Initialize with 0, so we fetch a new token on the first request

    def get_access_token(self):
        # Check if the token is expired or doesn't exist
        if self.access_token is None or time.time() > self.token_expiry:
            self.access_token = self._fetch_new_access_token()
        return self.access_token

    def _fetch_new_access_token(self):
        client_id = os.getenv("PAYPAL_CLIENT_ID")
        client_secret = os.getenv("PAYPAL_CLIENT_SECRET")
        
        # Print the environment variables to ensure they are being loaded correctly
        print(f"Client ID: {client_id}")
        print(f"Client Secret: {client_secret}")

        auth_response = requests.post(
            'https://api.sandbox.paypal.com/v1/oauth2/token',
            headers={"Accept": "application/json", "Accept-Language": "en_US"},
            data={"grant_type": "client_credentials"},
            auth=(client_id, client_secret)
        )
        
        response_json = auth_response.json()
        print("PayPal Response:", response_json)  # Log the entire response for debugging

        if 'access_token' in response_json:
            self.token_expiry = time.time() + response_json['expires_in'] - 60  # Subtract 60 seconds for a buffer
            return response_json['access_token']
        else:
            raise ValueError(f"Failed to obtain access token: {response_json}")

# Create an instance of PayPalClient to manage access tokens
paypal_client = PayPalClient()

@order_bp.route('/views/create-order', methods=['POST'])
def create_order():
    """
    Create an order with PayPal.
    This endpoint receives order details, gets an access token from PayPal, and then creates an order.
    """
    order_details = request.json  # Get the order details from the request
    try:
        access_token = paypal_client.get_access_token()  # Get PayPal access token
    except ValueError as e:
        print("Error getting PayPal access token:", str(e))
        traceback.print_exc()  # Print the full stack trace to the console
        return jsonify({"error": str(e)}), 500

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"  # Authorization token
    }

    try:
        # Send request to PayPal to create an order
        response = requests.post(
            'https://api.sandbox.paypal.com/v2/checkout/orders',
            headers=headers,
            json={
                "intent": order_details['intent'],
                "purchase_units": order_details['purchase_units']
            }
        )

        # Check if the order creation was successful
        if response.status_code == 201:
            return jsonify({"orderID": response.json()['id']})  # Return the order ID
        else:
            print("Error creating PayPal order:", response.json())
            traceback.print_exc()  # Print the full stack trace
            return jsonify({"error": response.json()}), response.status_code  # Return the error message
    except Exception as e:
        print("Unexpected error during order creation:", str(e))
        traceback.print_exc()  # This will print the full stack trace to the console
        return jsonify({"error": "Internal Server Error"}), 500
