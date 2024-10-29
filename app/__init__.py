from flask import Flask
from .config import Config # importando class Config de archivo "config.py"

from .database import db # importando los modelos de tablas de la bbdd


""" Crea la app de Flask """
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) # utilizando config importado
    
    db.init_app(app)
    
    return app