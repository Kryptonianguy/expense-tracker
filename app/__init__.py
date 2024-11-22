from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    from app.controllers.routes import main
    app.register_blueprint(main)

    return app