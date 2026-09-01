from flask import Flask
import random
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    number = random.randint(1,100) + random.randint(1,1000)
    if number == 777:
        extra = "I JUST HIT THE JACKPOTTT"
    elif number == 666:
        extra = "Ruh roh, he coming."
    elif number == 67:
        extra = "67676767676767"
    elif number == 2 or number == 1100:
        extra = "Damn, thats rare."
    elif number == 550:
        extra = "WERE HALF WAY THERE WOOOOOAOO LIVIN ON A PRAYER"
    elif number == 911 or number == 111 or number == 105:
        extra = "WEE WOO WEE WOO"
    elif number == 351:
        extra = "Funny number"
    else:
        extra = ""
    return f"Sup brah, this is my web site. Also {number} {extra}"

@app.route("/about")
def about():
    return "<h1>Sup brah, this is some information declaration welcome to my nation type stuff.<h1>"

@app.route("/fih")
def fih():
    return f"Sup brah, this is some fih that you can catch in the game how to fih.\n<ul>this is a list about fih<ul>"

@app.route("/genius")
def genius():
    time = random.randint(1,24)
    if time > 12:
        return "Good Afternoon."
    elif time < 12:
        return "Good Morning."

@app.route("/date")
def date():
    return str(datetime.now())

@app.errorhandler(404)
def eroor404(e):
    return "you suc"

app.run(debug = True)