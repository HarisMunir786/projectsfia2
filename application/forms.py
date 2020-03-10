from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User, Sport, Modus, Participant

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

class GenerateForm(FlaskForm):
	sport = SelectField('Sport',
		validators=[
			DataRequired()
		], choices = [("Football", "Basketball","Volleyball", "Rugby", "Hockey", "Tennis", "Table Tennis", "Badminton")]
	}

	modus = SelectField('Modus',
		validators=[
			DataRequired()
		], choices = [("Semi Finals", "Quarter Finals","8th Finals", "16th Finals", "32nd Finals")]
	)

	participant = StringField('Participant',
		validators=[
			DataRequired()
		]
	)


