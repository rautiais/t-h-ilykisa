from db import db
from sqlalchemy.sql import text
from flask import session

def check_event_cat(event_cat_name):
    event_cat_name_lower = event_cat_name.lower()
    sql = text("""SELECT id FROM event_cat
               WHERE (LOWER(event_cat_name)=:event_cat_name)""")
    result = db.session.execute(sql, {"event_cat_name":event_cat_name_lower})
    event_cat_id = result.fetchone()
    return event_cat_id[0] if event_cat_id else False

def new_event_cat(event_cat_name):
    event_cat_name_lower = event_cat_name.lower()
    try:
        sql = text("""INSERT INTO event_cat (event_cat_name) 
                   VALUES (:event_cat_name)""")
        db.session.execute(sql, {"event_cat_name":event_cat_name_lower})
        db.session.commit()
        return True
    except:
        return False

def all_event_cats():
    sql = text("""SELECT id, event_cat_name 
               FROM event_cat ORDER BY event_cat_name""")
    result = db.session.execute(sql)
    return result.fetchall()

def list_events_in_cat(cat_id):
    sql = text("""SELECT e.id, e.event_name, c.event_cat_name
               FROM events e JOIN event_cat c ON e.event_cat_id = c.id
               WHERE c.id=:cat_id""")
    result = db.session.execute(sql, {"cat_id": cat_id})
    return result.fetchall()
