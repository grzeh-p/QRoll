import sqlite3
from flask_restful import reqparse, Resource


class CreateCharacter(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("OWNER_ID", type=int, required=True, help="fill Owner plz")
    parser.add_argument("NAME", type=str, required=True, help="fill Name plz")
    parser.add_argument("CHAR_LEVEL", type=int, required=True, help="fill LvL plz")
    parser.add_argument("BAB_progression", type=int, required=True, help="fill BAB plz")
    parser.add_argument("SAV_FORT", type=int, required=True, help="fill Fort plz")
    parser.add_argument("SAV_DEX", type=int, required=True, help="fill Dex plz")
    parser.add_argument("SAV_WILL", type=int, required=True, help="fill Will plz")

    def post(self):
        data = CreateCharacter.parser.parse_args()
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "INSERT INTO characters VALUES(?,?,?,?,?,?,?)"
        try:
            cursor.execute(query, (data["OWNER_ID"], data["NAME"], data["CHAR_LEVEL"], data["BAB_progression"], data["SAV_FORT"], data["SAV_DEX"], data["SAV_WILL"]))
        except sqlite3.IntegrityError:
            return {"message": "Character already exists"}, 400
        connection.commit()
        connection.close()
        return {"message": "Character created successsfuly"}, 201
