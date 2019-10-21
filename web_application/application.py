from flask import Flask, render_template

app = Flask("shreya")

@app.route("/")
def homepage():
    return "Hello World"

@app.route("/a")
def body():
    return render_template("webpage.html") 

app.run()