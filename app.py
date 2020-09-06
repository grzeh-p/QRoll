import sqlite3
from flask import Flask, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from Characters.create_character import CreateCharacter
from Users.Create_User import UserRegister

db = SQLAlchemy()
app = Flask(__name__)
api = Api(app)


@app.route('/')
def start():
    return render_template("start.html")


@app.route('/user_add')
def user_register():
    return render_template("user_add.html")


@app.route('/user_list')
def user_list():
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute("select ID, USERNAME from users")

    rows = cur.fetchall()
    return render_template("user_list.html", rows=rows)


@app.route('/char_add')
def char_add():
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute("select ID, USERNAME from users")

    rows = cur.fetchall()
    return render_template("char_add.html", rows=rows)


@app.route('/char_list')
def char_list():
    # return render_template("char_list.html")
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute("select * from characters")

    rows = cur.fetchall()
    return render_template("char_list.html", rows=rows)


@app.route('/Roll')
def roll_main():
    return render_template("roll.html")


api.add_resource(CreateCharacter, '/char_add')
api.add_resource(UserRegister, '/user_add')

if __name__ == '__main__':
    app.run()
