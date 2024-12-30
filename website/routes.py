from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from .forms import AddExpenseForm
from .models import Expense
from . import db

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

@routes.route('/add-expense', methods=['GET', 'POST'])
@login_required
def add_expense():
    form = AddExpenseForm()
    if form.validate_on_submit():
        # Creating an Expense instance and save it to the database
        new_expense = Expense(
            expense_name = form.expense_name.data,
            expense_amount = form.expense_amount.data,
            expense_category = form.expense_category.data,
            expense_date = form.expense_date.data,
            description = form.description.data,
            user_id = current_user.id
        )

        db.session.add(new_expense)
        db.session.commit()

        # Handle the form submission (e.g., save to the database)
        flash('Expense added successfully!', 'success')
        return redirect(url_for('routes.add_expense'))
    elif form.errors:
        flash(form.errors, category='error')
    return render_template('addExpense.html', user = current_user, form = form)

@routes.route('/view-expense')
@login_required
def view_expense():
    return render_template('viewExpense.html', user = current_user)