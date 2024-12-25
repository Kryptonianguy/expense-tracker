from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
# from flask import redirect, url_for

class AddExpenseForm(FlaskForm):
    expense_name = StringField('Expense Name', validators=[DataRequired()])
    expense_amount = FloatField('Amount', validators=[DataRequired()])
    expense_category = StringField('Category')
    description = TextAreaField('Description', validators=[DataRequired()])
    submit_button = SubmitField('Save')
    # Cancel button is handled in the HTML template