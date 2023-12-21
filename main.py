from flask import Flask, render_template, redirect, session, request
import os
import pymysql

app = Flask(__name__)
app.secret_key = "talkwave"
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


@app.route("/account_registration", methods=['post'])
def account_registration():
    account_name = request.form.get("account_name")
    account_username = request.form.get("account_username")
    account_email = request.form.get("account_email")
    account_password = request.form.get("account_password")
    gender = request.form.get("gender")
    profile = request.files.get("profile")
    print(profile)
    path = app_root + "/profiles/" + profile.filename
    profile.save(path)
    count = cursor.execute("select * from account where account_username = '"+str(account_username)+"' or account_email = '"+str(account_email)+"'")
    if count == 0:
        cursor.execute("insert into account(account_name, account_username, account_email, account_password, gender, profile) value('"+str(account_name)+"', '"+str(account_username)+"', '"+str(account_email)+"', '"+str(account_password)+"', '"+str(gender)+"', '"+str(profile.filename)+"')")
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
        account = cursor.fetchall()
        account = account[0]
        session['account_id'] = account[0]
        session['role'] = 'account'
        return redirect("/navbar")
    else:
        return render_template("msg.html", message="Please Enter Valid Credentials")


@app.route("/account")
def account():
    account_id = session['account_id']
    print(account_id)
    cursor.execute("select * from account where account_id = '"+str(account_id)+"'")
    account = cursor.fetchone()
    print(account)
    return render_template("account.html", account=account)


@app.route("/get_friends", methods=['get'])
def get_friends():
    search = request.args.get("search")
    if search != "":
        cursor.execute("select * from account where account_username like'%" + search + "%'")
    else:
        return "No Users Are Found"
    friends = cursor.fetchall()
    return render_template("get_friends.html", friends=friends)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


app.run(debug=True)
