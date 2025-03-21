from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///favoritefilms.db"
db = SQLAlchemy(app)



@app.route("/")
def loginer():
    return render_template("home.html")


@app.route("/login")
def homer():
    return render_template("login.html")



if __name__ == "__main__":
    app.run(debug=True)