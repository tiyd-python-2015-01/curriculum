from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route("/")
def hello_form():
    return render_template("hello.html")

@app.route("/hello", methods=["POST"])
def say_hello():
    return render_template("say_hello.html", name=request.form['first_name'])

if __name__ == "__main__":
    app.run(debug=True)
