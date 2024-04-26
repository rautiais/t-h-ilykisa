from db import db
from sqlalchemy.sql import text
from flask import session

def check_event_cat(event_cat_name):
    sql = text("""SELECT id FROM event_cat
               WHERE event_cat_name=:event_cat_name""")
    result = db.session.execute(sql, {"event_cat_name":event_cat_name})
    event_cat_id = result.fetchone()
    return event_cat_id[0] if event_cat_id else False

def new_event_cat(event_cat_name):
    try:
        sql = text("""INSERT INTO event_cat (event_cat_name) 
                   VALUES (:event_cat_name)""")
        db.session.execute(sql, {"event_cat_name":event_cat_name})
        db.session.commit()
    except:
        return False
    return event_cat_name.fetchone()
