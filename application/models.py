from application import db
from application import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(100), nullable=False)
	password = db.Column(db.String(500), nullable=False)
	def __repr__(self):
		return ''.join([
			'Name: ', self.name, '\r\n',
			'Email: ', self.email
			])

class Participant(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	participant = db.Column(db.String(100), nullable=False)
	tournamentid = db.Column(db.Integer,db.ForeignKey('tournament.id'))
	def __repr__(self):
		return ''.join([
			self.participant
			])

class Randomstorage(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	randomstorage = db.Column(db.String(50), nullable=False)
	participantid = db.Column(db.Integer, db.ForeignKey('participant.id'))
	tournamentid = db.Column(db.Integer, db.ForeignKey('tournament.id'))
	def __repr__(self):
		return ''.join([
			'Random Storage: ', self.randomstorage
			])

class Tournament(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	thirty2ndfinals = db.Column(db.String(50), nullable=False)
	sixteenthfinals = db.Column(db.String(50), nullable=False)
	eighthfinals = db.Column(db.String(50), nullable=False)
	quarterfinals = db.Column(db.String(50), nullable=False)
	semifinals = db.Column(db.String(50), nullable=False)
	final = db.Column(db.String(50), nullable=False)
	participantid = db.Column(db.Integer, db.ForeignKey('participant.id'))
	randomstorageid = db.Column(db.Integer, db.ForeignKey('randomstorage.id'))
	def __repr__(self):
		return ''.join([
			'32ndfinals: ', self.thirty2ndfinals, '\r\n',
			'16thfinals: ', self.sixteenthfinals, '\r\n',
			'8thfinals: ', self.eighthfinals, '\r\n',
			'Quarterfinals: ', self.quarterfinals, '\r\n',
			'Semifinals: ', self.semifinals, '\r\n',
			'Final: ', self.final
			])
