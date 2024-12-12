"""
Configuration module for the MasterBlog application.
"""


class Config:
    """
    Configuration class for the application.

    Attributes:
        SQLALCHEMY_DATABASE_URI (str): URI for the database.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Disable SQLAlchemy modification tracking.
    """

    SQLALCHEMY_DATABASE_URI = "sqlite:///masterblog.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
