from db import db
from sqlalchemy.sql import text
from flask import session

def check_group(group_name):
    group_name_lower = group_name.lower()
    sql = text("""SELECT id FROM groups 
               WHERE LOWER(group_name)=LOWER(:group_name)""")
    result = db.session.execute(sql, {"group_name":group_name_lower})
    group_id = result.fetchone()
    return group_id[0] if group_id else False

def new_group(group_name):
    group_name_lower = group_name.lower()
    try:
        sql = text("""INSERT INTO groups (member_id, group_name) 
                   VALUES (:member_id,:new_group) RETURNING id""")
        db.session.execute(sql, {"member_id":session["user_id"], "new_group":group_name_lower})
        db.session.commit()
        return True
    except:
        return False

def join_group(group_id):
    try:
        sql = text("""INSERT INTO user_info (group_id, user_id) 
                   VALUES (:group_id, :user_id)""")
        db.session.execute(sql, {"group_id":group_id, "user_id":session["user_id"]})
        db.session.commit()
        return True
    except:
        return False
    
def users_all_groups():
    sql = text("""SELECT u.group_id, g.group_name 
               FROM user_info u INNER JOIN groups g
               ON g.id = u.group_id
               WHERE u.user_id=:user_id""")
    result = db.session.execute(sql, {"user_id":session["user_id"]})
    return result.fetchall()

def list_users(group_id):
    sql = text("""SELECT u.id, u.username, g.group_name
                FROM user_info ui
               JOIN users u ON ui.user_id = u.id
               JOIN groups g ON ui.group_id = g.id
               WHERE g.id=:group_id""")
    result = db.session.execute(sql, {"group_id":group_id})
    return result.fetchall()

def check_access(group_id):
    sql = text("""SELECT u.id FROM user_info u
                WHERE u.group_id=:group_id AND u.user_id:=user_id""")
    result = db.session.execute(sql, {"group_id":group_id, "user_id":session["user_id"]})
    if result.fetchone():
        return True
    return False

def list_all_groups():
    sql = text("""SELECT id, group_name FROM groups
               ORDER BY group_name""")
    result = db.session.execute(sql)
    return result.fetchall()

def log_group_event(user_id, group_id, event_id):
    sql = text("""SELECT points FROM events
               WHERE id=:event_id""")
    result = db.session.execute(sql, {"event_id":event_id})
    event_points_row = result.fetchone()

    if event_points_row is None:
        return False

    event_points = event_points_row[0]

    sql = text("""INSERT INTO user_events (user_id, group_id, event_id, points)
               VALUES (:user_id, :group_id, :event_id, :points)""")
    db.session.execute(sql, {"user_id":user_id, "group_id":group_id, "event_id":event_id, "points":event_points})
    db.session.commit()
    return True

def calculate_scores(group_id):
    sql = text("""SELECT u.username, SUM(ue.points) AS total_points
               FROM user_events ue JOIN users u
               ON u.id = ue.user_id
               WHERE ue.group_id =:group_id
               GROUP BY u.username
               ORDER BY total_points DESC""")
    result = db.session.execute(sql, {"group_id":group_id})
    return result.fetchall()