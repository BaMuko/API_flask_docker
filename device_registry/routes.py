from .players import PlayersApi, PlayerApi, UserDBs, UserDB
from .auth import SignupApi, LoginApi
from .reset_password import ForgotPassword, ResetPassword

def initialize_routes(api):
	api.add_resource(PlayersApi, '/api/players')
	api.add_resource(PlayerApi, '/api/players/<id>')

	api.add_resource(SignupApi, '/api/auth/signup')
	api.add_resource(LoginApi, '/api/auth/login')

	api.add_resource(ForgotPassword, '/api/auth/forgot')
	api.add_resource(ResetPassword, '/api/auth/reset')
	#nevím, jak jinak se dostat do DB, kde se schraňují informaci o uživatelých
	api.add_resource(UserDBs, '/api/checkdb')
	api.add_resource(UserDB, '/api/checkdb/delete/<email>')