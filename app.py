# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Welcome to the Expense Tracker !"

# if __name__ == "__main__":
#     app.run(debug=True)

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)