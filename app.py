from flask import Flask, render_template, request, redirect, url_for, session
from db_config import get_db_connection


app = Flask(__name__)
app.secret_key = 'secret_key_here'  

ADMIN_USERNAME = "admin@gmail.com"
ADMIN_PASSWORD = "admin123"

# ------------------------------------ LOGIN ------------------------------------
@app.route('/', methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        if email == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["loggedin"] = True
            session["email"] = ADMIN_USERNAME
            session["role"] = "admin"
            return redirect(url_for("home"))
        
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM students WHERE email =%s AND password=%s", (email, password))
        student = cur.fetchone()

        cur.close()
        conn.close()

        if student:
            session['loggedin'] = True
            session['username'] = student[2] + student[3]
            session['email'] = student[4]
            session['phone'] = student[5]
            session['password'] = student[7]
            session['address'] = student[6]
            session['role'] = student[8]
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username or password!'

    return render_template('login.html', msg=msg)
    