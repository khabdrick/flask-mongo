from flask import render_template, url_for, flash, redirect, request
from app import app, db
from app.models import Post
from app.forms import PostForm


@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)


@app.route("/post/new", methods=["GET", "POST"])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created!", "success")
        return redirect(url_for("home"))
    return render_template("post.html", title="New Post", form=form)


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("detail.html", title=post.title, post=post)


@app.route("/post/<int:post_id>/edit", methods=["GET", "POST"])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Your post has been updated!", "success")
        return redirect(url_for("post", post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template("edit_post.html", title="Edit Post", form=form)


@app.route("/post/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted!", "success")
    return redirect(url_for("home"))


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.args.get("query")
    posts = Post.query.filter(
        Post.title.contains(query) | Post.content.contains(query)
    ).all()
    return render_template("index.html", posts=posts)
