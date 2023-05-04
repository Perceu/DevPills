"""
Pagina simples com flask

Dependencias:

>> pip3 install flask

Executando:

>> flask --app server run

server.py:
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"