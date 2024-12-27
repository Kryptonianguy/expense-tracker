from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange
# from flask import redirect, url_for

class AddExpenseForm(FlaskForm):
    expense_name = StringField('Expense Name', validators=[DataRequired(), Length(max=80)])
    expense_amount = FloatField('Amount', validators=[DataRequired(), NumberRange(min=0)])
    expense_category = StringField('Category')
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=150)])
    submit_button = SubmitField('Save')
    # Cancel button is handled in the HTML template