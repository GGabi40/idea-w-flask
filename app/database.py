from flask_sqlalchemy import SQLAlchemy # https://flask-sqlalchemy.readthedocs.io/en/stable/models/
from werkzeug.security import generate_password_hash, check_password_hash # importa método para encriptar password

db = SQLAlchemy()


""" Crear todas las tablas """
class User(db.Model):
    __tablename__ = 'users' # nombre para la tabla
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    cellphone = db.Column(db.String(50), nullable=False)
    avatar = db.Column(db.String(250), nullable=True)
    
    def __repr__(self):
        return '<User %r>' % self.username
    
    """ Encripta password """
    def setPassword(self, password):
        # DOCS: https://werkzeug.palletsprojects.com/en/stable/utils/
        self.password = generate_password_hash(password)
        
    def checkPassword(self, password):
        return check_password_hash(self.password, password)



""" Tabla de Categorías """
class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    


""" Tabla de Ideas """
class Ideas(db.Model):
    __tablename__ = 'ideas'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    is_public = db.Column(db.Boolean, default=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    category = db.relationship('Category', backref=db.backref('ideas', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('ideas', lazy=True))


""" QUÉ ES ESO
category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    db.ForeignKey(): define clave foránea que referencia columna id en tabla categories
    ondelete='CASCADE': especifica que, si se elimina algo de la tabla categories, tambien se eliminarán
                    todas las ideas relacionadas a esa categoría.


category = db.relationship('Category', backref=db.backref('ideas', lazy=True))
    db.relationship('Category'): establece relación entre Idea y Category,
                    permitiendo acceder a la categoría asociada al aidea directamente
                    con idea.category
    
    backref=db.backref('ideas', lazy=True): Crea un acceso inverso, desde la instancia
                    Category se puede acceder a todas las ideas usando category.ideas
    
    lazy=True: Define como se cargan los datos relacionados. Se cargarán automaticamente
            cuando se acceden a ellas.


Básicamente, facilita el acceso directo, permitiendo navegar entre los datos
"""