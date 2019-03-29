from flask import Flask
import pyodbc as dba
app = Flask(__name__)

@app.route("/")
def hello():
    a = 20
    return "hellolaoaksdword"
