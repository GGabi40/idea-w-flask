from .database import *

""" Método de creación de la BBDD """
def create_db():
    db.drop_all()
    db.create_all()


""" Método de inicialización de nuestra BBDD """
def init_db():
    create_db()
    
    # user admin app
    admin = User(
        name = 'Gabi',
        lastName = 'Baptista',
        email = 'gabibc2000@hotmail.com',
        is_admin = True,
        username = 'ggabi',
        cellphone = '3415555555'
    )
    admin.setPassword("123")
    db.session.add(admin)
    db.session.commit()
    