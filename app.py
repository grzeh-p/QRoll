from flask import Flask, render_template
from flask_restful import Api
from Characters.Create_Character import CreateCharacter
from Users.Create_User import UserRegister


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
    return render_template("user_list.html")


@app.route('/char_add')
def char_add():
    return render_template("char_add.html")


@app.route('/char_list')
def char_list():
    return render_template("char_list.html")


@app.route('/Roll')
def roll_main():
    return render_template("Roll.html")


api.add_resource(CreateCharacter, '/char_add')
api.add_resource(UserRegister, '/user_add')

if __name__ == '__main__':
    app.run()
