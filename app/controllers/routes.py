from flask import Blueprint, render_template

# Define a Blueprint for the main routes of the application
main = Blueprint('main', __name__)

# Route for the home page
@main.route('/')
def home():
    # Render the home page template
    return render_template('index.html')