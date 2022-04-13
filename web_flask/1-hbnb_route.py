#!/usr/bin/python3
"""
Script starts Flask web application
listens on 0.0.0.0 port 5000
Routes '/' displays "Hello HBNB!"
'/hbnb' dislpays "HBNB"
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



if __name__ == "__main__":
    app.run(host="0.0.0.0")
