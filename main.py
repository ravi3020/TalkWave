from flask import Flask, render_template, redirect, session, request
import os
import pymysql

app = Flask(__name__)
conn = pymysql.connect(host="localhost", user="root", password="root", db="TalkWave")
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


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/account_registration")
def account_registration():
    account_name = request.args.get("account_name")
    account_username = request.args.get("account_username")
    account_email = request.args.get("account_email")
    account_password = request.args.get("account_password")
    gender = request.args.get("gender")
    count = cursor.execute("select * from account where account_username = '"+str(account_username)+"' or account_email = '"+str(account_email)+"'")
    if count == 0:
        cursor.execute("insert into account(account_name, account_username, account_email, account_password, gender) value('"+str(account_name)+"', '"+str(account_username)+"', '"+str(account_email)+"', '"+str(account_password)+"', '"+str(gender)+"')")
        conn.commit()
        return redirect("/")
    else:
        return render_template("msg.html", message="Already Exist")


@app.route("/account_login")
def account_login():
    account_username = request.args.get("account_username")
    account_password = request.args.get("account_password")
    count = cursor.execute("select * from account where account_username = '"+str(account_username)+"' and account_password = '"+str(account_password)+"'")
    if count > 0:
        return redirect("/navbar")
    else:
        return render_template("msg.html", message="Please Enter Valid Credentials")


app.run(debug=True)
