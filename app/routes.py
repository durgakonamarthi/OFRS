from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/login')
def login():
    return render_template('login.html', title='Log In')

@app.route('/signup')
def signup():
    return render_template('signup.html', title='Sign Up')

# Add more routes as needed
