from flask import Flask, render_template, redirect, session, request
import os
import pymysql

app = Flask(__name__)
conn = pymysql.connect(host="localhost", user="root", password="Luther@1234", db="TalkWave")
cursor = conn.cursor()

app_root = os.path.dirname(os.path.abspath(__file__))
app_root = app_root+"/static"


@app.route("/navbar")
def navbar():
    return render_template("navbar.html")

@app.route("/")
def login():
    return render_template("login.html")



app.run(debug=True)
