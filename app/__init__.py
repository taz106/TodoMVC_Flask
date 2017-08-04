import os

from flask import Flask

# PYMONGO IMPORT AND INITIALIZATION
from flask_pymongo import PyMongo
mongo = PyMongo()

# IMPORT APP CONFIG
from config import Config

# IMPORTING BLUEPRINT OBJECT
from app.controllers.index import index
from app.controllers.todo import todo

def create_app():
    ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    app = Flask(__name__, template_folder=ASSETS_DIR, static_folder=ASSETS_DIR)
    app.register_blueprint(index, url_prefix="/")
    app.register_blueprint(todo, url_prefix="/api/v1")
    
    app.config.from_object(Config)
    app.config['MONGO_DBNAME'] = "sodingtodoapp"
    app.config['MONGO_URI'] = "mongodb://soding:sodingsoding@ds117093.mlab.com:17093/sodingtodoapp"
    # app.config['MONGO_HOST'] = '127.0.0.1'
    # app.config['MONGO_PORT'] = 27017
    # app.config['MONGO_DBNAME'] = 'TodoAppDb001'

    mongo.init_app(app)

    return app 