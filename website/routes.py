from flask import Blueprint, render_template
from flask_login import login_required, current_user

routes = Blueprint('routes', __name__)

@routes.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

# Route for Dash Board Pages.
@routes.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user = current_user)

@routes.route('/add-expense')
@login_required
def add_expense():
    return render_template('addExpense.html', user = current_user)

@routes.route('/view-expense')
@login_required
def view_expense():
    return render_template('viewExpense.html', user = current_user)