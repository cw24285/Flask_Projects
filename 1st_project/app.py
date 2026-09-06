from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    name = "Seb"
    address = "308 Negra Arroyo Lane, Albuquerque, New Mexico"
    return render_template("home.html", Name1 = name, Address1 = address)

@app.route("/about")
def about():
    name = "Seb"
    return render_template("about.html", Name1 = name)

@app.errorhandler(404)
def error404(e):
    return "you suc"

app.run(debug = True)