from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)

    with app.app_context():
        # Import and initialize routes
        from .routes import init_routes

        init_routes(app)

        # Create database tables
        db.create_all()

    return app
