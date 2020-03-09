# import render_template, url_for, redirect and request function from the flask module
from flask import render_template, url_for, redirect, request
# import the app, db and bcrypt object from the ./application/__init__.py
from application import app, db, bcrypt
# import the models from the ./application/models.py
from application.models import User
# import login_user, current_user, logout_user, login_required function from flask_login
from flask_login import login_user, current_user, logout_user, login_required
# import RegistrationForm and LoginForm from ./application/forms.py
from application.forms import LoginForm, RegistrationForm

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

@app.route('/register')
def register():
	return render_template('register.html', title='Register')

@app.route('/login')
def login():
        return render_template('login.html', title='Login')
