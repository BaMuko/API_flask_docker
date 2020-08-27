from flask import request, render_template
from flask_jwt_extended import create_access_token, decode_token
from database.models import User
from flask_restful import Resource
import datetime

from services.mail_service import send_mail
from .config import ADMINS

from .errors import SchemaValidationError, InternalServerError, \
EmailDoesnotExistsError, BadTokenError
from jwt.exceptions import ExpiredSignature, DecodeError, \
InvalidTokenError

class ForgotPassword(Resource):
	def post(self):
		url = request.host_url + 'reset/'

		body = request.get_json()
		email = body.get('email')


		user = User.objects.get(email=email)


		expires = datetime.timedelta(hours=24)
		reset_token = create_access_token(str(user.id), expires_delta=expires)


		return send_mail('[Player-bag] Reset Your Password',
						sender = ADMINS[0],
						recipients=[user.email],
							text_body=render_template('email/reset_password.txt', url=url + reset_token),
							html_body=render_template('email/reset_password.html', url=url + reset_token))
		



class ResetPassword(Resource):
	def post(self):
		url = request.host_url + 'reset/'
		#try:
		body = request.get_json()
		reset_token = body.get('reset_token')
		password = body.get('password')


		if not reset_token or not password:
			raise SchemaValidationError

		user_id = decode_token(reset_token) ['identity']

		user = User.objects.get(id=user_id)

		user.modify(password=password)
		user.hash_password()
		user.save()

		return send_mail('[Player-bag] Password reset successful',
						sender='support@player-bag.com',
						recipients=[user.email],
						text_body='Password reset was successful.',
						html_body='<p>Password reset was successful</p>')

		except SchemaValidationError:
			raise SchemaValidationError
		except ExpiredSignature:
			raise ExpiredTokenError
		except (DecodeError, InvalidTokenError):
			raise BadTokenError
		except Exception as e:
			raise InternalServerError
