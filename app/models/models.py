from app import db

# Define the Expense model
class Expense(db.Model):
    """
    Represents an expense record in the database.
    """
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each expense
    description = db.Column(db.String(255), nullable=False)  # Description of the expense
    amount = db.Column(db.Float, nullable=False)  # Expense amount
    date = db.Column(db.Date, nullable=False)  # Date of the expense

    def __repr__(self):
        """
        Provides a string representation of an Expense instance for debugging.
        """
        return f"<Expense {self.description}>"