from flask import Flask
from config import Config
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



moment = Moment()
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager() 


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    moment.init_app(app)
    db.init_app(app) 
    migrate.init_app(app, db) 
    login.init_app(app)
  
    



    with app.app_context():
        from app.blueprints.main import bp as main_bp
        app.register_blueprint(main_bp)

        from app.blueprints.pokemon import bp as pokemon_bp
        app.register_blueprint(pokemon_bp)

    return app