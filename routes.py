from app import app
from flask import redirect, render_template, request
import users
import groups_main
#import events_main

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Wrong username or password")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]        
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", messages="The passwords don't match")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Registration failed")        

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/new_group", methods=["POST"])
def new_group():
    group_name = request.form["new_group"]
    return render_template("groups.html")

@app.route("/join_group", methods=["POST"])
def join_group():
    group_name = request.form["group_name"]
    return group_name

@app.route("/groups")
def groups():
   # all_groups = groups_main.list_groups()
    return render_template("groups.html")    #,all_groups=all_groups)

@app.route("/event_cat", methods=["GET"])
def event_cat():
    return render_template("event_cat.html")


    # event_cat_name = request.form["event_cat_name"]
    # all_events = event_cat.fetchall())
    # if event_cat_name not in all_events:
    #     return render_template("event_cat.html")
    # else:
    #     return render_template("error.html", message="This event category is not unique")        

