from flask import Flask, render_template

print(__name__)
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/tracks")
def tracks_page():
    return render_template("tracks.html")

@app.errorhandler(404)
def error404(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)