"""
Initialization module for the MasterBlog application.
"""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """
    Factory function to create and configure the Flask application.

    Returns:
        Flask: Configured Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Set a secret key
    app.secret_key = os.urandom(24)

    db.init_app(app)

    # Import and register Blueprints
    from app.routes import blueprint

    app.register_blueprint(blueprint, url_prefix="/")

    with app.app_context():
        db.create_all()

    return app
