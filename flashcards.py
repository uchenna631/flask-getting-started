from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template('welcome.html') 

@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())

counter = 1