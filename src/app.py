from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
# import utils as utils

# Configure app
app = Flask(__name__)

# Connect to database 
db = SQL("sqlite:///app.db")

#Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# def name_from_session():
#   return session.get("name")

# name = name_from_session()

#My Controller
@app.route("/", methods = ["POST","GET"])
def index():
  
  name = session.get("name")
  
  if not name:
    return redirect("/login")
  else:
    return render_template("index.html", name = name)

  
@app.route("/login", methods = ["POST","GET"])
def login():
  if request.method == "POST":
    session["name"] = request.form.get("name")
    return redirect("/")
  if "name" in session:
    return redirect("/")
  return render_template("login.html")
  
@app.route("/logout")
def logout():
  session.clear()
  return redirect("/")  

@app.route("/lists", methods = ["GET","POST"])
def lists():
  name = session.get("name")
  if request.method == "GET":
    tasks = db.execute("SELECT * FROM tasks")
    return render_template("lists/lists.html",name = name, tasks = tasks)
  

  
@app.route("/lists/add", methods=["GET"])
def add():
  name = session.get("name")
  if request.method == "GET":
    return render_template("lists/add-list.html", name = name)
  
  
if __name__ == "__main__":
  app.run(debug=True)  
  