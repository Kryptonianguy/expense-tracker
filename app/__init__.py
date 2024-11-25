from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Initialize SQLAlchemy instance
db = SQLAlchemy()

def create_app():
    """Factory function to create and configure the Flask application."""
    app = Flask(__name__)

    # Configure the application with database settings
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the SQLAlchemy extension with the app
    db.init_app(app)

    # Import and register blueprints
    from app.controllers.routes import main
    app.register_blueprint(main)

    return app