#!/usr/bin/python3
"""
script that starts a Flask web application
with port number and localhost
which uses render_template from flask
checks whether number is even or odd
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
    return render_template('number_template.html', number=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    parity = "even" if n % 2 == 0 else "odd"
    return render_template('odd_or_even_template.html',
                           number=n, parity=parity)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
