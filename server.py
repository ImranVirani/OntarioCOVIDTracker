# Flask Web app that will serve the website that allows an email to be added to the database so that anyone can recieve email updates.
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
