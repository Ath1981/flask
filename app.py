from flask import Flask,jsonify
app = Flask(__name__)
app.debug = True 

personas = ["brayan","juan","pablo"]


@app.route("/")
def hello_world():
    return jsonify(personas)