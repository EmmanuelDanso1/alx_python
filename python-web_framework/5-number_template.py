#!/usr/bin/python3
"""
script that starts a Flask web application
with port number and localhost
which uses render_template from flask
"""
from flask import Flask, render_template
"""
Creating an instance of class from Flask import
and storing it in a variable app
"""
app = Flask(__name__)
"""
using @app.route to map '/' to the url
"""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    creating a method from the class Flask
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

"""
displaying text and replacing underscore
with text
"""

@app.route('/c/<text>', strict_slashes=False)
def c_replace_text(text):
    """
    replacing underscore with text
    """
    formatted_text = text.replace('_', ' ')
    return "C {}".format(formatted_text)

@app.route('/python/', defaults={'text': 'is cool'},
           strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    formatted_text = text.replace('_', ' ') if text else 'is cool'
    return "Python {}".format(formatted_text)

"""
displays 'n' only if n is an integer
"""

@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    return "{} is a number".format(n)

"""
template html and python script
"""
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('templates/5-number.html', number=n)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
