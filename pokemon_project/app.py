from flask import Flask, render_template, redirect, request, url_for
import sqlite3

app = Flask (__name__)

DB = "Flask_Projects/pokemon_project/pokemon.db"

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/pokemon")
def pokemon():
    conn = get_db()
    pokemon = conn.execute("SELECT * FROM pokemon LIMIT 20").fetchall()
    conn.close
    return render_template("pokemon.html", pokemon=pokemon)

if __name__ == "__main__":
    app.run(debug=True)