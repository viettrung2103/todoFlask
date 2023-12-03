# from cs50 import SQL
from flask import Flask, redirect, render_template, request, session, \
                  url_for, flash
                  
from flask_session import Session
from database.db import db
from routes import register_routes

# import utils as utils

# Configure app
app = Flask(__name__)

# Connect to database 
# db = SQL("sqlite:///app.db")

#Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#register routes to our app
register_routes(app)
  
  
if __name__ == "__main__":
  app.run(debug=True)  
  