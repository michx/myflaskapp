import requests
from flask import Flask
from flask import render_template 
app = Flask(__name__)
    

@app.route("/")
def index():
    return render_template("index.html",title='Welcome', username='Mich')

def create_app():
    app.run(host='0.0.0.0', port=81)