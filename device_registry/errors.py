class InternalServerError(Exception):
	pass

class SchemaValidationError(Exception):
	pass

class PlayerAlreadyExistsError(Exception):
	pass

class UpdatingPlayerError(Exception):
	pass

class DeletingPlayerError(Exception):
	pass

class PlayerNotExistsError(Exception):
	pass

class EmailAlreadyExistsError(Exception):
	pass

class EmailDoesnotExistsError(Exception):
	pass

class BadTokenError(Exception):
	pass

class UnauthorizedError(Exception):
	pass


errors = {
	"InternalServerError": {
		"message": "Request is missing required fields",
		"status": 500
	},
	"SchemaValidationError": {
		"message": "Request is missing required fields.",
		"status": 400
	},
	"PlayerAlreadyExistsError": {
		"message": "Movie with given name already exists.",
		"status": 400
	},
	"UpdatingPlayerError": {
		"message": "Updating movie added by other is forbidden.",
		"status": 403
	},
	"DeletingPlayerError": {
		"message": "Deleting player added by other is forbidden.",
		"status": 403
	},
	"PlayerNotExistsError": {
		"message": "Player with given id doesn't exist.",
		"status": 400
	},
	"EmailAlreadyExistsError": {
		"message": "User with given email address already exists.",
		"status": 400
	},
	"UnauthorizedError": {
		"message": "Invalid username or password.",
		"status": 401
	},
	"EmailDoesnotExistsError": {
		"message": "Couldn't find the user with given email address.",
		"status": 400
	},
	"BadTokenError": {
		"message": "Invalid token",
		"status": 403
	}
}