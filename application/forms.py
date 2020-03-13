from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User, Participant, Randomstorage, Tournament

class RegistrationForm(FlaskForm):
	name = StringField('Name',
		validators = [
			DataRequired()
		]
	)

	email = StringField('Email',
		validators = [
			DataRequired(),
			Email()
		]
	)

	password = PasswordField('Password',
		validators = [
			DataRequired()
		]
	)

	confirm_password = PasswordField('Confirm Password',
		validators = [
			DataRequired(),
			EqualTo('password')
		]
	)

	submit = SubmitField('Sign Up')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()

		if user:
			raise ValidationError('Email already in use')

class LoginForm(FlaskForm):
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		]
	)

	password = PasswordField('Password',
		validators=[
			DataRequired()
		]
	)

	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class EnterForm(FlaskForm):
	sport = SelectField('Sport',
		validators=[
			DataRequired()
		]
	)

	totalnumber = SelectField('Total Number',
		validators=[
			DataRequired()
		]
	)

	participant = StringField('Participant',
		validators=[
			DataRequired()
		]
	)
	submit = SubmitField('Enter')

class GenerateForm(FlaskForm):
	sport = SelectField('Sport',
		validators=[
			DataRequired()
		]
	)

	totalnumber = SelectField('Total Number',
		validators=[
			DataRequired()
		]
	)

	participant = StringField('Participant',
		validators=[
			DataRequired()
		]
	)

	submit = SubmitField('Generate')

#class GenerateForm(FlaskForm):
#	sport = SelectField('Sport',
#		validators=[
#			DataRequired()
#		], choices = [("FOOTBALL","Football"),("BASKETBALL","Basketball"),("VOLLEYBALL","Volleyball"),("RUGBY", "Rugby"), ("HOCKEY", "Hockey"), ("TENNIS", "Tennis"), ("TABLE TENNIS", "Table Tennis"), ("BADMINTON", "Badminton")]
#	)
#
#	modus = SelectField('Modus',
#		validators=[
#			DataRequired()
#		], choices = [("SEMI FINALS", "Semi Finals")]
#	)
#
#	participant = StringField('Participant',
#		validators=[
#			DataRequired()
#		]
#	)
#	submit = SubmitField('Generate')
