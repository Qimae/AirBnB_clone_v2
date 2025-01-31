#!/usr/bin/python3
"""
Script starts Flask web application
listens on 0.0.0.0 port 5000
Routes '/' displays "Hello HBNB!"
'/hbnb' dislpays "HBNB"
'/c/<text>' displys C
'/python/(<text>) displays Python is cool
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Displays 'HELLO HBNB!'"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hello():
    """Displays HBNB"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """DIsplays C"""
    text = text.replace("_", " ")
    return "C %s" % text

@app.route('/python/(<text>)', strict_slashes=False)
def python_text(text="is cool"):
    """Displays Python"""
    text = text.replace("_", " ")
    return "Python %s" % text



if __name__ == "__main__":
    app.run(host="0.0.0.0")
