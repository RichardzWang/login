#Richard Wang
#SoftDev
#Period9

from flask import Flask, render_template, request, session, url_for, redirect
from utils import authenticator

app = Flask(__name__)

app.secret_key = '\x90\xfb\x0f6\x1dY\xa5i\x93+m\x83\xd8\xd9\xad\x91}\xef\x95]_\xe2i\xde\xcc\xb7\x03c\x83\xf3\xd1J'

@app.route("/")
def login():
    if 'username' in session:
        return redirect(url_for('welcome'))
    return render_template('login.html')

@app.route("/authenticate/", methods = ['POST'])
def auth():
    #REGISTER
    if 'username' in session:
        return redirect(url_for('welcome'))
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
    if 'username' in session:
        session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = 'TRUE'
    app.run()
