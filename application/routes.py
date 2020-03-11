# import render_template, url_for, redirect and request function from the flask module
from flask import render_template, url_for, redirect, request
# import the app, db and bcrypt object from the ./application/__init__.py
from application import app, db, bcrypt
# import the models from the ./application/models.py
from application.models import User, Sport, Modus, Participant
# import login_user, current_user, logout_user, login_required function from flask_login
from flask_login import login_user, current_user, logout_user, login_required
# import RegistrationForm and LoginForm from ./application/forms.py
from application.forms import LoginForm, RegistrationForm, EnterForm, GenerateForm

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		hash_pw = bcrypt.generate_password_hash(form.password.data)
		user = User(name=form.name.data, email=form.email.data, password=hash_pw)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('login'))
	form = LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('enter'))
	return render_template('login.html', title='Login', form=form)

@app.route('/enter', methods=['GET', 'POST'])
#@login_required()
def enter():
	form = EnterForm()
	#if form.validate_on_submit():
	return render_template('enter.html', title='Enter the particpant', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/generate', methods=['GET', 'POST'])
def generate():
	form = GenerateForm()
#	if form.validate_on_submit():
	return render_template('generate.html', title='Random Generator', form=form)
