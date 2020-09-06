import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password