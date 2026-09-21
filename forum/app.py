from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask (__name__)

DB = "Flask_Projects/forum/forum.db"

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute("""CREATE TABLE IF NOT EXISTS posts (
                        post_id INTEGER PRIMARY KEY,
                        author TEXT NOT NULL,
                        message TEXT NOT NULL)""")
    conn.commit()
    conn.close()

init_db()

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/forum")
def forum():
    conn = get_db()
    posts = conn.execute("SELECT * FROM posts ORDER BY post_id DESC").fetchall()
    conn.close()
    return render_template("forum.html", posts = posts)

@app.route("/post", methods=["POST"]) 
def new_post(): 
    author = request.form["author"] 
    message = request.form["message"] 
    return f"Got a post from {author}: {message}" 

@app.route("/")
def redirect_to_forum():
    return redirect("/forum")

if __name__ == "__main__":
    app.run(debug=True)