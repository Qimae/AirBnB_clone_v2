#!/usr/bin/python3
"""
Script starts Flask web app
listening on 0.0.0.0:5000
Route '/' displays "Hello HBNB!"
"""
from flask import Flask

app = Flask(__name__)



@app.route('/', strict_slashes=False)
def hello_route():
    """Displays String"""
    return "Hello HBNB!"



if __name__ == "__main__":
    app.run(host="0.0.0.0")
