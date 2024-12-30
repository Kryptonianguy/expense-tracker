from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, TextAreaField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from datetime import date
# from flask import redirect, url_for

class AddExpenseForm(FlaskForm):

    def validExpenseDate(form, field):
        if field.data > date.today():
            raise ValidationError('Expense date cannot be in the future')

    expense_name = StringField('Expense Name', validators=[DataRequired(), Length(max=80)])
    expense_amount = FloatField('Amount', validators=[DataRequired(), NumberRange(min=0)])
    expense_category = StringField('Category')
    expense_date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired(), validExpenseDate])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=150)])
    submit_button = SubmitField('Save')
    # Cancel button is handled in the HTML template