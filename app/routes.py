"""
Routes module for the MasterBlog application.
"""

from flask import Blueprint, flash, redirect, render_template, request, url_for

from app import db
from app.models import BlogPost

# Define a Blueprint
blueprint = Blueprint("blog", __name__)


@blueprint.route("/")
def index():
    """
    Render the homepage with a list of all blog posts.

    Returns:
        str: Rendered template for the homepage.
    """
    posts = BlogPost.query.all()
    return render_template("index.html", posts=posts)


@blueprint.route("/post/<int:id>")
def post(id):
    """
    Render a detailed view of a single blog post.

    Args:
        id (int): ID of the blog post.

    Returns:
        str: Rendered template for the post.
    """
    post = BlogPost.query.get_or_404(id)
    return render_template("post.html", post=post)


@blueprint.route("/add", methods=["GET", "POST"])
def add():
    """
    Add a new blog post.

    Returns:
        str: Rendered template for adding a post or a redirect to the homepage.
    """
    if request.method == "POST":
        author = request.form["author"]
        title = request.form["title"]
        content = request.form["content"]

        if author and title and content:
            new_post = BlogPost(author=author, title=title, content=content)
            db.session.add(new_post)
            db.session.commit()
            flash("Post added successfully!", "success")
            return redirect(url_for("blog.index"))
        else:
            flash("Please fill in all fields", "danger")

    return render_template("add.html")


@blueprint.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    """
    Edit an existing blog post.

    Args:
        id (int): ID of the blog post to edit.

    Returns:
        str: Rendered template for editing a post or a redirect to the post's detail view.
    """
    post = BlogPost.query.get_or_404(id)

    if request.method == "POST":
        post.author = request.form["author"]
        post.title = request.form["title"]
        post.content = request.form["content"]
        db.session.commit()
        flash("Post updated successfully!", "success")
        return redirect(url_for("blog.post", id=id))

    return render_template("edit.html", post=post)


@blueprint.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    """
    Delete a blog post.

    Args:
        id (int): ID of the blog post to delete.

    Returns:
        werkzeug.wrappers.response.Response: Redirect to the homepage.
    """
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted successfully!", "success")
    return redirect(url_for("blog.index"))


@blueprint.route("/like/<int:id>", methods=["POST"])
def like(id):
    """
    Increment the like count of a blog post.

    Args:
        id (int): ID of the blog post to like.

    Returns:
        werkzeug.wrappers.response.Response: Redirect to the homepage.
    """
    post = BlogPost.query.get_or_404(id)
    post.likes += 1
    db.session.commit()
    return redirect(url_for("blog.index"))
