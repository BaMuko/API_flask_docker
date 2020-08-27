from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class PlayerDB(db.Document):
	name = db.StringField(required =True)
	score = db.IntField(required = True, unique = False)
	#id = db.IntField(required = True, primary_key = True)
	added_by = db.ReferenceField('User')


class User(db.Document):
	email = db.EmailField(required=True, unique=True)
	password = db.StringField(required=True, unique=True)
	players = db.ListField(db.ReferenceField('PlayerDB', reverse_delete_rule=db.PULL))

	def hash_password(self):
		self.password = generate_password_hash(self.password).decode('utf8')

	def check_password(self, password):
		return check_password_hash(self.password, password)

User.register_delete_rule(PlayerDB, 'added_by', db.CASCADE)