from flask import Flask, render_template, url_for, redirect
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/aboutMe/")
def aboutMe():
    return render_template("aboutMe.html")

@app.route("/math/")
def mathTest():
    return render_template("mathTest.html")

@app.route("/images/")
def imagesPage():
    return render_template("imagesPage.html")

if __name__ == "__main__":
    app.run(debug=false,host="0.0.0.0")
    
