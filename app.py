#Richard Wang
#SoftDev
#Period9

from flask import Flask, render_template, request
from utils import authenticator

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/authenticate/", methods = ['POST'])
def auth():
    #REGISTER
    if (request.form["action"] == "REGISTER"):
        if (authenticator.register(request.form["username"], request.form["password"])):
            return render_template('login.html', message = "You have been registered")
        else:
            return render_template('login.html', message = "Your username has been taken")
    #LOGIN
    if (request.form["action"] == "LOGIN"):
        number = (authenticator.auth(request.form["username"],request.form["password"]))
    if number == -1:
        return render_template('authenticate.html', message1 = "Access Granted", message2 = "Successfully logged in")
    if number == -2:
        return render_template('authenticate.html', message1 = "Access Denied", message2 = "Your password is incorrect")
    if number == -3:
        return render_template('authenticate.html', message1 = "Access Denied", message2 = "Your username does not exist")
    return "error"

if __name__ == '__main__':
    app.debug = 'TRUE'
    app.run()
