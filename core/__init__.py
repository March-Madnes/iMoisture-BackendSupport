import os

from cryptography.fernet import Fernet
from flask import Flask
from flask_cors import CORS

# fernet key for encrypting and decrypting data
# fernet = Fernet(os.getenv("FERNET_KEY"))

app = Flask(__name__)
CORS(app)
app.config["SECRET_KEY"] = os.getenv("SQL_ACLCHEMY_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

from core.views import home

app.register_blueprint(home.home)
