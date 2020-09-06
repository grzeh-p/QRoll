import sqlite3
from flask_restful import reqparse, Resource


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="fill this plz")
    parser.add_argument("password", type=str, required=True, help="cannot be empty")

    def post(self):
        data = UserRegister.parser.parse_args()
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "INSERT INTO users VALUES(null, ?,?)"
        try:
            cursor.execute(query, (data["username"], data["password"]))
        except sqlite3.IntegrityError:
            return {"message": "user already exists"}, 400
        connection.commit()
        connection.close()
        return {"message": "user created successsfuly"}, 201