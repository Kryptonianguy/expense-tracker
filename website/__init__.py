from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
import os

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

# Base directory and database file path
basedir = os.path.abspath(os.path.dirname(__file__))
DB_NAME = os.path.join(basedir, "expense_tracker.db")

def create_app():
    app = Flask(__name__)

    # csrf = CSRFProtect(app)

    # App configuration
    app.config['SECRET_KEY'] = 'asderdsads'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    #importing routes and blueprints here
    from .routes import routes
    from .auth import auth
    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import models and create the database
    from .models import User

    create_database(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    with app.app_context():
        if not os.path.exists(DB_NAME):
            db.create_all()
            print('Database Created')