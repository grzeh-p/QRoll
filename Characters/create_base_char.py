import sqlite3

connection = sqlite3.connect("../data.db")

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text unique, password text);"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS characters(OWNER_ID INTEGER, NAME TEXT, CHAR_LEVEL INTEGER, BAB_progression INTEGER, SAV_FORT INTEGER, SAV_DEX INTEGER, SAV_WILL INTEGER, FOREIGN KEY(owner_id) REFERENCES users(id));"
cursor.execute(create_table)


connection.commit()
connection.close()


if __name__ == '__main__':
    pass
