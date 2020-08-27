from database.models import PlayerDB, User
from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource


from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

from .errors import SchemaValidationError, PlayerAlreadyExistsError, \
InternalServerError, UpdatingPlayerError, DeletingPlayerError, PlayerNotExistsError


class  PlayersApi(Resource):
    @jwt_required
    def get(self):
        players = PlayerDB.objects.to_json()
        return Response(players, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        try:
            user_id = get_jwt_identity()
            args = request.get_json()
            user = User.objects.get(id=user_id)
            player = PlayerDB(**args, added_by=user)
            player.save()
            user.update(push__players=player)
            user.save()
            id = player.id
            return {"id": str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise PlayerAlreadyExistsError
        except Exception as e:
            raise InternalServerError




class PlayerApi(Resource):
    @jwt_required
    def get(self, id):
        try:
            player = PlayerDB.objects.get(id=id).to_json()
            return Response(player, mimetype="application/json", status=200) 
        except DoesNotExist:
            raise PlayerNotExistsError
        except Exception:
            raise InternalServerError

    @jwt_required
    def put(self, id):
        try:
            user_id = get_jwt_identity()
            player = PlayerDB.objects.get(id=id, added_by=user_id)
            args = request.get_json()
            PlayerDB.objects.get(id=id).update(**args)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExit:
            raise UpdatingPlayerError
        except Exception:
            raise InternalServerError


    @jwt_required
    def delete(self, id):
        try:
            user_id = get_jwt_identity()
            player = PlayerDB.objects.get(id=id, added_by=user_id)
            player.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingPlayerError
        except Exception:
            raise InternalServerError



#nevím, jak jinak se dostat do DB, kde se schraňuje obsah o uživatelích
class UserDBs(Resource):
    def get(self):
        users = User.objects.to_json()
        return Response(users, mimetype="application/json", status=200)

class UserDB(Resource):
        def delete(self, email):
            try:
                user = User.objects.get(email=email)
                user.delete()
                return '', 200
            except DoesNotExist:
                raise DeletingPlayerError
            except Exception:
                raise InternalServerError
