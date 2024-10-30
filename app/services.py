from .database import *

""" Retornar usuario a partir del username """
def get_user_by_username(username):
    return User.query.filter_by(username=username)


""" Registra un usuario nuevo en la BBDD """
def register_user(user_data):
    user = User(
        name=user_data['name'],
        lastName=user_data['lastName'],
        email=user_data['email'],
        password=user_data['password'],
        is_admin=user_data['is_admin'],
        username=user_data['username'],
        cellphone=user_data['cellphone']
    )
    user.set_password(user_data['password'])
    
    db.session.add(user)
    db.session.commit()