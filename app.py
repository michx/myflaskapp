import requests, app
from app import render_template 
app = app.Flask(__name__)
    

@app.route("/")
def index():
    return render_template("index.html",title='Welcome', username='Mich')

