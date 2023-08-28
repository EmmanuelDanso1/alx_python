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
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
