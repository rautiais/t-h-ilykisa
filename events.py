from db import db
from sqlalchemy.sql import text
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def event_cat(event_cat_name):
    try:
        sql = text("INSERT INTO event_cat (event_cat_name) VALUES (:event_cat_name)")
        db.session.execute(sql, {"event_cat_name":event_cat_name})
        db.session.commit()
    except:
        return False
    return event_cat_name.fetchone()