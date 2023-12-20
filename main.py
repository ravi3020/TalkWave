from flask import Flask, render_template, redirect, session, request
import os
import pymysql

app = Flask(__name__)
conn = pymysql.connect(host="localhost", user="root", password="Sharmi@2020", db="TalkWave")
cursor = conn.cursor()

app_root = os.path.dirname(os.path.abspath(__file__))
app_root = app_root+"/static"


@app.route("/")
def logo_animate():
    return render_template("logo_animate.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/navbar")
def navbar():
    return render_template("navbar.html")



app.run(debug=True)
