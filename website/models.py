from . import db
from flask_login import UserMixin
from datetime import datetime, timezone

class User(db.Model, UserMixin):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    def __init__(self, first_name, email, password):
        self.first_name = first_name
        self.email = email
        self.password = password

class Expense(db.Model):
    __tablename__ = 'Expense'

    id = db.Column(db.Integer, primary_key=True)
    expense_name = db.Column(db.String(80), nullable=False)
    expense_amount = db.Column(db.Float, nullable=False)
    expense_category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(150), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    def __init__(self, expense_name, expense_amount, expense_category, description, user_id):
        self.expense_name = expense_name
        self.expense_amount = expense_amount
        self.expense_category = expense_category
        self.description = description
        self.user_id = user_id