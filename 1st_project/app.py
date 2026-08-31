from flask import Flask
import random
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    number = random.randint(1,100) + random.randint(1,2)
    return (f"Sup brah, this is my web site. Also {number}")

@app.route("/about")
def about():
    return ("<h1>Sup brah, this is some information declaration welcome to my nation type stuff.<h1>")

@app.route("/fih")
def fih():
    return (f"Sup brah, this is some fih that you can catch in the game how to fih.\n<ul>this is a list about fih<ul>")

@app.route("/genius")
def genius():
    time = random.randint(1,24)
    if time > 12:
        return ("Good Afternoon.")
    elif time < 12:
        return ("Good Morning.")

@app.route("/date")
def date():
    return str(datetime.now())

@app.errorhandler(404)
def eroor404(e):
    return "you suc"

app.run(debug = True)