""" Clase de configuracion de flask """
class Config:
    SECRET_KEY = '123ideas' # Llave secreta utilizada por Flask para sesiones, cookies y protección contra ataques CSRF
    
    # URI (Uniform Resource Identifier) para la base de datos SQLAlchemy.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../ideas.db' # se configura en donde está la BBDD SQlite
    
    # Desactiva el seguimiento de modificaciones en SQLAlchemy, lo cual ahorra recursos
    # No es necesario en la mayoría de los casos y puede generar un pequeño impacto en el rendimiento si se deja en True
    SQLALCHEMY_TRACK_MODIFICATIONS = False