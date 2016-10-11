#Richard Wang
#SoftDev
#Period9

from flask import Flask, render_template, request, session, url_for, redirect
from utils import authenticator

app = Flask(__name__)

app.secret_key = "secret?"

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/authenticate/", methods = ['POST'])
def auth():
    #REGISTER
    if (request.form["action"] == "REGISTER"):
        return render_template('login.html', message = authenticator.register(request.form["username"], request.form["password"]))

    #LOGIN
    if (request.form["action"] == "LOGIN"):
        number = (authenticator.auth(request.form["username"],request.form["password"]))
    if number == -1:
        session['username'] = request.form['username']
        return redirect(url_for('welcome'))
    if number == -2:
        return render_template('login.html', message = "Your password is incorrect")
    if number == -3:
        return render_template('login.html', message = "Your username does not exist")
    return "error"

@app.route("/welcome/")
def welcome():
    if 'username' in session:
        return render_template('welcome.html', name = session['username'])
    else:
        return "Not logged in"

@app.route("/logout/")
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = 'TRUE'
    app.run()
