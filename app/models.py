"""
Models module for the MasterBlog application.
"""

from . import db


class BlogPost(db.Model):
    """
    BlogPost model representing a blog post in the database.

    Attributes:
        id (int): Primary key for the blog post.
        author (str): Author of the blog post.
        title (str): Title of the blog post.
        content (str): Content of the blog post.
        likes (int): Number of likes for the blog post.
    """

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    likes = db.Column(db.Integer, default=0)
