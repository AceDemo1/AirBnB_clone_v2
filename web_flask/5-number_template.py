#!/usr/bin/python3
"""This module starts a Flask web application must be listening on 0.0.0.0,
port 5000"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """The method displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """The method displays 'hbnb'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """The method displays 'C' following by text"""
    new_text = text.replace("_", " ")
    return "C {}".format(new_text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """The method displays 'Python' following text"""
    new_text = text.replace("_", " ")
    return "Python {}".format(new_text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """The method displays 'n is a number' if n is an int"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_n(n):
    """The method displays an HTML page if n is an int"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
