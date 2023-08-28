#!/usr/bin/python3
"""
script that starts a Flask web application
with port number and localhost
"""
from flask import Flask
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
    formatted_text = text.replace('_', '')
    return "C {}".format(formatted_text)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
