# import Flask class from the flask module
from flask import Flask
# import SQLAlchemy class from the flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# import Bcrypt class from the flask_bcrypt
from flask_bcrypt import Bcrypt
# import LoginManager class from flask_login
from flask_login import LoginManager
from os import getenv
import os

# create a new instance of Flask and store it in app
app = Flask(__name__)
# create a new instance of bcrypt and store it in Bcrypt(app)
bcrypt = Bcrypt(app)

# create a new instance of login_manager and store it in LoginManager(app)
login_manager = LoginManager(app)
# create a new view of login_manager view
login_manager.login_view = 'login'

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('MY_SECRET_KEY')
db = SQLAlchemy(app)

# import the ./application/routes.py file
from application import routes
