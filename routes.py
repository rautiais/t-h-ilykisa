from app import app
from flask import redirect, render_template, request, session


@app.route("/")
def index():
    return render_template("index.html")
    #result = db.session.execute(text("SELECT content FROM messages"))
    #messages = result.fetchall()
    #return render_template("index.html",count=len(messages),messages=messages)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # TODO: check username and password
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/new")
def new():
    return render_template("new.html")

# @app.route("/send", methods=["POST"])
# def send():
#     content = request.form["content"]
#     sql = text("INSERT INTO messages (content) VALUES (:content)")
#     db.session.execute(sql, {"content":content})
#     db.session.commit()
#     return redirect("/")

# @app.route("/page1")
# def page1():
#     return "page1"

# @app.route("/page2")
# def page2():
#     return "page2"

# @app.route("/form")
# def form():
#     return render_template("form.html")

# @app.route("/result", methods=["POST"])
# def result():
#     return render_template("result.html", name=request.form["name"])

