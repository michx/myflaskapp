import requests, flask

app = flask.Flask(__name__)
    

    
  
    

@app.route("/"):
    return render_template("index.html"title='Welcome', username='Mich')

