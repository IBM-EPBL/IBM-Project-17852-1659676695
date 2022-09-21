from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<P>Hello, From home</p>"

@app.route("/blog")
def blog():
    return "<h1>MY Blog</H1>"

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')