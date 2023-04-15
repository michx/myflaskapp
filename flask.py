import requests, flask
from flask import render_template 
app = flask.Flask(__name__)
    

@app.route("/")
def index():
    return render_template("index.html"title='Welcome', username='Mich')

