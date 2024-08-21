from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS for the entire Flask application
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    from app.views.register import register_bp
    from app.views.store import store_bp
    from app.views.product import product_bp
    from app.views.order import order_bp
    from app.views.login import login_bp
    from app.views.profile import profile_bp

    app.register_blueprint(register_bp)
    app.register_blueprint(store_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(profile_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)  # Ensure Flask runs in debug mode

    import os

print("SECRET_KEY:", os.getenv("SECRET_KEY"))
print("PAYPAL_CLIENT_ID:", os.getenv("PAYPAL_CLIENT_ID"))
print("PAYPAL_CLIENT_SECRET:", os.getenv("PAYPAL_CLIENT_SECRET"))

