from flask import Flask, redirect, url_for, render_template, send_file

app = Flask(__name__)
app.config.from_object("config")

@app.route("/")
def home():
    return "Hello World"

@app.route("/about")
def about():
    return render_template("index.html", pageTitle='My Home page')

@app.route("/travel_blog")
def travelblog():
    return render_template("travel.html", pageTitle='My travel blog')

@app.route("/food_blog")
def foodblog():
    return render_template("food.html", pageTitle='My food blog')

@app.route("/signupforupdates")
def signupforupdates():
    return render_template("signupforupdates", pageTitle="Signup")

if __name__ == "__main__":
    app.run()