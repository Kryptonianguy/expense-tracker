from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150))

    def __init__(self, first_name, email, password):
        self.first_name = first_name
        self.email = email
        self.password = password