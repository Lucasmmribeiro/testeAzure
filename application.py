from flask import Flask
import pyodbc as dba
app = Flask(__name__)

@app.route("/")
def hello():
    a = "a vida e bela"
    return a
