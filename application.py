from flask import Flask
import pyodbc as dba
app = Flask(__name__)

@app.route("/")
def hello():
    return "helo"
