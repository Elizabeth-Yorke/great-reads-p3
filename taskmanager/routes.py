from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa

@app.route("/")
def home():
    return render_template("base.html")
