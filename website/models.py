from . import db
from flask_login import UserMixin
from datetime import date
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150))
    created_at = db.Column(db.DateTime, default=func.now())  # Use func.now()
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())

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
    expense_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(150), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    created_at = db.Column(db.DateTime, default=func.now())  # Use func.now()
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())

    def __init__(self, expense_name, expense_amount, expense_category, expense_date, description, user_id):
        self.expense_name = expense_name
        self.expense_amount = expense_amount
        self.expense_category = expense_category
        self.expense_date = expense_date
        self.description = description
        self.user_id = user_id