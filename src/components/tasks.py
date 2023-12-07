from database.db import db

def get_all_tasks():
  tasks = db.execute("SELECT * FROM tasks")
  return tasks

def get_task_by_id(task_id):
  task = db.execute("SELECT * FROM tasks WHERE task_id = (?)",task_id)[0]
  return task

def edit_task_by_id(task_id,task_name,description,is_done):
  db.execute("UPDATE tasks SET name = ?, description = ?, is_done = ? WHERE task_id = ?",task_name, description, is_done, task_id)
  return

def delete_task_by_id(task_id):
  db.execute("DELETE FROM tasks WHERE task_id = ?",task_id)
  return
  
def add_task(task_name, description):
  db.execute("INSERT INTO tasks (name,description) VALUES (?,?)", task_name,description)
  return