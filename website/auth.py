from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)

# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')

#         user = User.query.filter_by(email=email).first()

#         if user and check_password_hash(user.password, password):
#             flash('Logged in successfully!', category='success')
#             login_user(user, remember=True)
#             return redirect(url_for('routes.home'))

#         else:
#             flash('Please insert valid data.', category='error')

#             # ✅ **Check if the request is from an API (JSON request)**
#             if request.is_json:
#                 return jsonify({"error": "Invalid credentials"}), 401  # API response

#     return render_template('login.html', user=current_user)

#Login, SignUp and Logout Routes.
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('routes.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Please insert valid data.', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        first_name = request.form.get('firstname')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email = email).first()

        if user:
            flash('Email Already Exists !', category='error')
        elif len(first_name) < 2:
            flash('First name must be at least 2 characters long.', category='error')
        elif len(email) < 3:
            flash('Email must be at least 3 characters long.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 8:
            flash('Password must be at least 8 characters long.', category='error')
        else:
            new_user = User(
                email=email,
                first_name=first_name,
                password=generate_password_hash(password1, method='pbkdf2:sha256')
                )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account Created Successfully !", category='success')
            # return redirect(url_for('auth.login'))
            return redirect(url_for('routes.home'))

    return render_template('signup.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
    # return render_template('home.html', user=current_user)