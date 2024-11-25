from app import create_app, db
from app.models.models import Expense

# Initialize the Flask application
app = create_app()

# Route to add a test expense (for demonstration purposes)
@app.route('/add-expense')
def add_expense():
    # Create a new Expense instance with sample data
    new_expense = Expense(
        description='Test Expense',
        amount=50.75,
        date='2024-11-25'
    )

    # Add the new expense to the database session and commit the transaction
    db.session.add(new_expense)
    db.session.commit()

    return "Expense Added Successfully!"

# Run the application in debug mode
if __name__ == "__main__":
    app.run(debug=True)