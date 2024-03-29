from flask import Flask, render_template
# to run flask --app app run --debug
app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/about/<username>")
def about_page(username):
    return f"<h1>This is the about page of {username}</h1>"
