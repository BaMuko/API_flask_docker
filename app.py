# Import the framework
from flask import Flask
from flask_restful import Api
from database.db import initialize_db


# pouziti k hashovani hesla
from flask_bcrypt import Bcrypt
#pouziti k oveření totoznosti uzivatele
from flask_jwt_extended import JWTManager
#zvládání chyb
from .errors import errors
#resetování hesla - odeslání mailu uživateli
from flask_mail import Mail


# Create an instance of Flask
app = Flask(__name__)
app.config.from_pyfile('config.py')
mail = Mail(app)

#imports requing app and mail
from .routes import initialize_routes

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


app.config['MONGODB_SETTINGS'] = {
    #if db is installed localy i can access it:
        "name": 'api',
        "host": 'mongo',
        "port": 27017
}

initialize_db(app)

initialize_routes(api)