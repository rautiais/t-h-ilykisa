from db import db
from sqlalchemy.sql import text
from flask import session

def new_group(group_name):
    try:
        sql = text("INSERT INTO groups (user_id, group_name) VALUES (:user_id, :group_name) RETURNING id")
        result = db.session.execute(sql, {"user_id":session["id"], "group_name":group_name})
        group_id = result.fetchone()[0]
        sql = text("INSERT INTO user_info (user_id, group_id) VALUES (:user_id, :group_id)")
        db.session.execute(sql, {"user_id": session["id"], "group_id":group_id})
        db.session.commit()
        return True
    except:
        return False

def join_group(group_id):
    try:
        sql = text("INSERT INTO user_info (user_id, group_id) VALUES (:user_id, :group_id)")
        db.session.execute(sql, {"user_id":session["id"], "group_id":group_id})
        db.session.commit()
        return True
    except:
        return False
    
def check_group(group_name):
    sql = text("SELECT id FROM groups WHERE group_name=:group_name")
    result = db.session.execute(sql, {"group_name":group_name})
    group_id = result.fetchone()

def all_groups():
    sql = text("""SELECT u.group_id, u.group_name 
               FROM user_info u LEFT JOIN groups g
               ON u.group_id = g.id""")
    result = db.session.execute(sql, {"user_id":session["id"]})
    return result.fetchall()

