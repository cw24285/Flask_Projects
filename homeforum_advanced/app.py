from flask import Flask, render_template, redirect
import sqlite3

app = Flask (__name__)

DB = "Flask_Projects/homeforum_advanced/users.db"

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute("""CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL)""")
    conn.commit()
    conn.close()

init_db()

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/signup")
def signup():
    conn = get_db()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return render_template("forum.html", users = users)

@app.route("/")
def redirect_to_forum():
    return redirect("/signup")

if __name__ == "__main__":
    app.run(debug=True)