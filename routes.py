from app import app
from flask import redirect, render_template, request, flash
import users
import groups_main
import events_main

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

        if not users.check_username(username):
            return render_template("error.html", message="The username is already taken")

        if len(username) <= 2 or len(username) >= 20:
            return render_template("error.html", message="The username must be between 2 and 20 characters")
        
        if len(password1) <= 7 or len(password1) >= 50:
            return render_template("error.html", message="The password must be between 7 and 50 characters")     
        
        if password1 != password2:
            return render_template("error.html", message="Passwords do not match")
        
        if users.register(username, password1):
            return redirect("/")
        
        else:
            return render_template("error.html", message="Registration failed")        

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/new_group", methods=["POST"])
def new_group():
    users.check_token(request.form["csrf_token"])
    group_name = request.form["new_group"]
    if groups_main.check_group(group_name):
        print("Group name is not unique")
        #flash("Group name is not unique")
        return render_template("error.html", message="Group name is not unique")
        #return redirect("/groups")
    else:
        if groups_main.new_group(group_name):
            print("Creating a group was successful")
            #flash("Creating a group was successful")
            return redirect("/groups")
        else:
            #flash("Error")
            print("Error")
            return render_template("error.html", message="Error, creating the group was not successful")
            #return redirect("/groups")

@app.route("/join_group", methods=["POST"])
def join_group():
    users.check_token(request.form["csrf_token"])

    if "join_group" not in request.form:
        #flash("Please provide a group name to join.")
        print("Please provide a group name to join.")
        return render_template("error.html", message="Error, please provide a group name to join.")
        #return redirect("/groups")
        
    group_name = request.form["join_group"]
    group_id = groups_main.check_group(group_name)

    if group_id:
        if groups_main.join_group(group_id):
            #flash("You joined the group")
            print("You joined the group")
            return redirect("/groups")
        else:
            #flash("You are already in the group")
            print("You are already in the group")
            return redirect("/groups")
    else:
        #flash("This group does not exist")
        print("This group does not exist")
        return render_template("error.html", message="Error, please provide a group name to join.")
        #return redirect("/groups")
        
@app.route("/groups")
def groups():
    my_groups = groups_main.all_groups()
    return render_template("groups.html", my_groups=my_groups)  

@app.route("/one_group/<int:group_id>")
def one_group(group_id):
    group_users = groups_main.list_users(group_id)
    if not group_users:
        return render_template("one_group.html", group_users=None)
    return render_template("one_group.html", group_users=group_users)

@app.route("/event_cat", methods=["GET"])
def event_cat():
    return render_template("event_cat.html")
