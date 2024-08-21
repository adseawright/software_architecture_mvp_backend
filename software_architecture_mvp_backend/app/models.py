from datetime import datetime, timezone
from . import db

# User model to represent users in the system
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each user
    username = db.Column(db.String(150), nullable=False)  # Username of the user
    email = db.Column(db.String(150), unique=True, nullable=False)  # Email of the user (must be unique)
    password = db.Column(db.String(200), nullable=False)  # Password of the user (hashed)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # Timestamp of user creation
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # Timestamp of last update

    # Method to convert User object to dictionary format
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

# Store model to represent stores in the system
class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each store
    name = db.Column(db.String(255), nullable=False)  # Name of the store
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key referencing the owner (user) of the store
    description = db.Column(db.String(255))  # Description of the store
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Timestamp of store creation
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())  # Timestamp of last update

    # Method to convert Store object to dictionary format
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'owner_id': self.owner_id,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

# Product model to represent products in the system
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each product
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)  # Foreign key referencing the store to which the product belongs
    name = db.Column(db.String(255), nullable=False)  # Name of the product
    description = db.Column(db.Text)  # Description of the product
    price = db.Column(db.Numeric, nullable=False)  # Price of the product
    unit = db.Column(db.String(50))  # Unit of measurement for the product (e.g., unit, dozen, pound)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Timestamp of product creation
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())  # Timestamp of last update

    # Method to convert Product object to dictionary format
    def to_dict(self):
        return {
            'id': self.id,
            'store_id': self.store_id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'unit': self.unit,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

# Sale model to represent sales transactions in the system
class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each sale
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)  # Foreign key referencing the product being sold
    quantity = db.Column(db.Integer, nullable=False)  # Quantity of the product sold
    total_price = db.Column(db.Numeric, nullable=False)  # Total price of the sale
    sale_date = db.Column(db.DateTime, default=db.func.current_timestamp())  # Timestamp of the sale
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Timestamp of sale record creation
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())  # Timestamp of last update

    # Method to convert Sale object to dictionary format
    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'total_price': self.total_price,
            'sale_date': self.sale_date,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }