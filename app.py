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
    if (authenticator.authenticator(request.form["username"],request.form["password"])):
        return render_template('authenticate.html', message1 = "Success!", message2 = "Successfully logged in")
    else:
        return render_template('authenticate.html', message1 = "Failure", message2 = "Failed to log in")

if __name__ == '__main__':
    app.debug = 'TRUE'
    app.run()
