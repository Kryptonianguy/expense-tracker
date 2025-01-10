from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from .forms import AddExpenseForm, UpdateExpenseForm
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
        error_messages = []
        for messages in form.errors.values():
            for message in messages:
                error_messages.append(message)

        for message in error_messages:
            flash(message, category='error')
    return render_template('addExpense.html', user = current_user, form = form)

@routes.route('/view-expense')
@login_required
def view_expense():
    expenses = Expense.query.filter_by(user_id=current_user.id).all()
    return render_template('viewExpense.html', user = current_user, expenses = expenses)

@routes.route('/update-expense/<int:id>', methods=['GET', 'POST'])
@login_required
def update_expense(id):
    form = UpdateExpenseForm()
    updateExpense = Expense.query.get_or_404(id)

    if request.method == "POST" and form.validate_on_submit():
        # Update the fields with form data
        updateExpense.expense_name = form.expense_name.data
        updateExpense.expense_amount = form.expense_amount.data
        updateExpense.expense_category = form.expense_category.data
        updateExpense.expense_date = form.expense_date.data
        updateExpense.description = form.description.data
        try:
            db.session.commit()
            flash('Expense Updated Successfully.', category='success')
            return redirect(url_for('routes.view_expense'))
        except Exception as e:
            return str(e)
    else:
        # Populate form with current expense data on GET
        form.expense_name.data = updateExpense.expense_name
        form.expense_amount.data = updateExpense.expense_amount
        form.expense_category.data = updateExpense.expense_category
        form.expense_date.data = updateExpense.expense_date
        form.description.data = updateExpense.description

    return render_template('updateExpense.html', user=current_user, form=form, updateExpense=updateExpense)

@routes.route('/delete-expense/<int:id>', methods=['POST'])
@login_required
def delete_expense(id):
    deletExpense = Expense.query.get_or_404(id)

    try:
        db.session.delete(deletExpense)
        db.session.commit()
        flash('Expense Deleted Successfully.', category='success')
        return redirect(url_for('routes.view_expense'))
    except Exception as e:
        return flash(str(e), category='error')

    # return render_template('deleteModal.html', user = current_user, deletExpense = deletExpense)