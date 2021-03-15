import sqlite3 as sql
db = sql.connect('panther.db')
pointer = db.cursor()

def get_user_prefix(user_name: str):
    pointer.execute("SELECT PREFIX FROM USERS WHERE NAME='"+user_name+"';")
    return pointer.fetchone()

def check_if_user_present(user_name: str):
    pointer.execute("SELECT * FROM USERS WHERE NAME='" + user_name + "';")
    return pointer.fetchone() != None

def get_no_users():
    pointer.execute("SELECT COUNT(ID) FROM USERS;")
    return pointer.fetchone()

def add_user(user_name: str, admin: bool = False):
    pointer.execute(f"INSERT INTO USERS(ID, NAME, ADMIN) VALUES({str(get_no_users[0])}, {user_name}, {admin} )")
    db.commit()
