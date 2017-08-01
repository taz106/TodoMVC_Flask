from flask import Flask
from flask_restful import Api

# PYMONGO IMPORT AND INITIALIZATION
from flask_pymongo import PyMongo
mongo = PyMongo()

# IMPORT APP CONFIG
from config import Config

# IMPORTING BLUEPRINT OBJECT
from app.controllers.user import user

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user, url_prefix="/api/v1")
    
    app.config.from_object(Config)
    app.config['MONGO_HOST'] = '127.0.0.1'
    app.config['MONGO_PORT'] = 27017
    app.config['MONGO_DBNAME'] = 'testAppDb001'

    mongo.init_app(app)

    return app 