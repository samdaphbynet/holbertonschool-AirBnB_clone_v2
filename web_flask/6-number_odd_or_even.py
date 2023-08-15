#!/usr/bin/python3
"""
    Script that starts a flask application
    and templates containe the pages html
    that check if number is odd or even
"""
from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    return "HBNB"


@app.route("/c/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/c/<text>")
def display_text(text):
    text = escape(text.replace("_", " "))
    return "C {}".format(text)


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>")
def display_text_python(text):
    text = escape(text.replace("_", " "))
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_template(n):
    return render_template("6-number_odd_or_even.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_odd_or_even(n):
    if n % 2 == 0:
        template = 'even'
    else:
        template = 'odd'
    return render_template("6-number_odd_or_even.html",
                           number=n, odd_even=template)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
