from flask import Flask, redirect, render_template, request, session, \
                  url_for, flash
from database.db import db

def register_routes(app):
  
  #My Controller
  @app.route("/", methods = ["POST","GET"])
  def index():
    
    name = session.get("name")
    
    if not name:
      return redirect(url_for("login"))
    else:
      return render_template("index.html", name = name)
    
  @app.route("/login", methods = ["POST","GET"])
  def login():
      if request.method == "POST":
        session["name"] = request.form.get("name")
        flash('You were successfully logged in')
        return redirect(url_for("index"))
      if "name" in session:
        return redirect(url_for("index"))
      return render_template("login.html")
    
  @app.route("/logout")
  def logout():
    session.clear()
    return redirect(url_for("index"))  
  
  @app.route("/lists", methods = ["GET","POST"])
  def lists():
    name = session.get("name")
    if request.method == "GET":
      tasks = db.execute("SELECT * FROM tasks")
      # print(tasks)
      return render_template("lists/lists.html",name = name, tasks = tasks)
    if request.method == "POST":
      task_id = request.form.get("task_id")
      return redirect(url_for("edit",task_id = task_id))
      
  def convert_is_done(text):
    if text == "on":
      return 1
    else:
      return 0

  @app.route("/edit/<task_id>",methods = ["GET","POST"])
  def edit(task_id):
    name = session.get("name")
    if request.method == "GET":
      #this return a list with one element
      task = db.execute("SELECT * FROM tasks WHERE task_id = (?)",task_id)[0]
      print(type(task["is_done"]))
      return render_template("lists/edit_list.html",task = task, name = name)
    else:
      task_id = request.form.get("task_id")
      task_name = request.form.get("task_name")
      description = request.form.get("description")
      is_done = convert_is_done(request.form.get("is_done"))
      db.execute("UPDATE tasks SET name = ?, description = ?, is_done = ? WHERE task_id = ?",task_name, description, is_done, task_id)
      # alert("Update successfuly")
      return redirect(url_for("lists"))
    
      
  @app.route("/delete/<task_id>", methods = ["GET","POST"])
  def delete(task_id):
    # name = session.get("name")
    if request.method == "GET":
      return redirect(url_for("lists"))
    else:
      db.execute("DELETE FROM tasks WHERE task_id = ?",task_id)
      # flash("Delete Successfully")
      return redirect(url_for("lists"))
    
    
  @app.route("/lists/add", methods=["GET","POST"])
  def add():
    name = session.get("name")
    if request.method == "GET":
      return render_template("lists/add-list.html", name = name)
    else:
      task_name = request.form.get("task-name")
      description = request.form.get("description")
      db.execute("INSERT INTO tasks (name,description) VALUES (?,?)", task_name,description)
      # print(request.form)
      return redirect(url_for("lists"))
      