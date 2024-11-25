from app import db, create_app
from app.models.models import Expense

# Initialize the Flask application
app = create_app()

# Create all database tables if they do not exist
with app.app_context():
    db.create_all()