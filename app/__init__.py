from flask import Flask
from .config import Config # importando class Config de archivo "config.py"

from .database import db # importando los modelos de tablas de la bbdd

from flask_login import LoginManager

from flask_bootstrap import Bootstrap # importa bootstrap
from .auth import auth # autenticación del usuario
from .ideas import ideas
from .models import UserModel


login_manager = LoginManager()
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(username):
    return UserModel.get(username)


""" Crea la app de Flask """
def create_app():
    app = Flask(__name__)
    
    bootstrap = Bootstrap(app) # inicializa bootstrap
    app.config.from_object(Config) # utilizando config importado
    app.register_blueprint(auth)
    app.register_blueprint(ideas)
    login_manager.init_app(app)
    
    db.init_app(app)
    
    return app