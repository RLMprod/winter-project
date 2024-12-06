from flask import Flask, url_for, redirect, render_template, request
import os
from config import data
app = Flask(__name__)

x = data


@app.route("/")
def main():
    return render_template('main.html', content=x)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for("user", usr=user))
    else:
        return render_template('login.html')


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
