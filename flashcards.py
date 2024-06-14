from flask import Flask, render_template
from model import db

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template('welcome.html', name='Fimber', age=31) 


@app.route("/card")
def card_view():
    title = 'Data science Terms',
    description = db["description"]  
    glossary = db['glossary']
    return render_template('card.html', title=title, description=description, glossary=glossary) 


