from db import db
from sqlalchemy.sql import text
from flask import session, abort
from werkzeug.security import check_password_hash, generate_password_hash
import secrets

def login(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["csrf_token"] = secrets.token_hex(16)
            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["csrf_token"]

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = text("""INSERT INTO users (username, password) 
                   VALUES (:username,:password)""")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)

def user_id():
    return session.get("user_id", 0)

def check_token(csrf_token):
    if session["csrf_token"] != csrf_token:
        abort(403)