from flask import render_template
from taskmanager import app, db
from taskmanager.models import Book, Review


@app.route("/")
def home():
    return render_template("base.html")
