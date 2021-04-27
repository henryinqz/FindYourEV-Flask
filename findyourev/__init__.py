from flask import Flask
from os import environ

app = Flask(__name__)
app.config["SECRET_KEY"] = environ.get("FINDYOUREV_SECRET_KEY")

from findyourev import routes