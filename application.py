from flask import Flask
import pyodbc as dba
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/teste/")
def hello2():
    return "FUCKIT!"

@app.route("/capic/")
def hello4():
    a = 20
    b = 40
    return a+b    