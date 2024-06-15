from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from .config import Config  # Correct import of Config class


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Use the correct Config class
    
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    
    from . import models, routes
    app.register_blueprint(routes.bp)  
    
    return app
