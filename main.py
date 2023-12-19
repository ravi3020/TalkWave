from flask import Flask, render_template, redirect, session, request
import os
import pymysql

app = Flask(__name__)
conn = pymysql.connect(host="localhost", user="root", password="root", db="TalkWave")
cursor = conn.cursor()

app_root = os.path.dirname(os.path.abspath(__file__))
app_root = app_root+"/static"

# @app.route("/")
# def head():
#     return render_template("head.html")

@app.route("/")
def login():
    return render_template("login.html")



app.run(debug=True)
