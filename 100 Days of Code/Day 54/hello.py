# save this as hello.py
import os
from wsgiref.simple_server import WSGIServer

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1> Hello, World! </h1>"


@app.route("/bye")
def bye():
    return "Bye!"


@app.route("/<name>")
def greet(name):
    return f"Hello, {name}!"


if __name__ == "__name__":
    os.environ.setdefault('FLASK_ENV', 'development')
    app.run(debug=True)