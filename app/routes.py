from flask import flash, redirect, render_template, request, url_for

from app import db
from app.models import BlogPost


def init_routes(app):
    @app.route("/")
    def index():
        posts = BlogPost.query.all()
        return render_template("index.html", posts=posts)

    @app.route("/post/<int:id>")
    def post(id):
        post = BlogPost.query.get_or_404(id)
        return render_template("post.html", post=post)

    @app.route("/add", methods=["GET", "POST"])
    def add():
        if request.method == "POST":
            author = request.form["author"]
            title = request.form["title"]
            content = request.form["content"]

            if author and title and content:
                new_post = BlogPost(author=author, title=title, content=content)
                db.session.add(new_post)
                db.session.commit()
                flash("Post added successfully!", "success")
                return redirect(url_for("index"))
            else:
                flash("Please fill in all fields", "danger")

        return render_template("add.html")

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit(id):
        post = BlogPost.query.get_or_404(id)

        if request.method == "POST":
            post.author = request.form["author"]
            post.title = request.form["title"]
            post.content = request.form["content"]
            db.session.commit()
            flash("Post updated successfully!", "success")
            return redirect(url_for("post", id=id))

        return render_template("edit.html", post=post)

    @app.route("/delete/<int:id>", methods=["POST"])
    def delete(id):
        post = BlogPost.query.get_or_404(id)
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted successfully!", "success")
        return redirect(url_for("index"))

    @app.route("/like/<int:id>", methods=["POST"])
    def like(id):
        post = BlogPost.query.get_or_404(id)
        post.likes += 1
        db.session.commit()
        return redirect(url_for("index"))
