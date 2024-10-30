from flask import Flask
from .config import Config # importando class Config de archivo "config.py"

from .database import db # importando los modelos de tablas de la bbdd

from flask_bootstrap import Bootstrap # importa bootstrap

from .auth import auth # autenticación del usuario


""" Crea la app de Flask """
def create_app():
    app = Flask(__name__)
    
    bootstrap = Bootstrap(app) # inicializa bootstrap
    app.config.from_object(Config) # utilizando config importado
    app.register_blueprint(auth)
    
    db.init_app(app)
    
    return app