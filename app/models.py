from flask_login import UserMixin
from .services import get_user_by_username

# https://flask-login.readthedocs.io/en/latest/

""" Model User - login """
class UserModel(UserMixin):
    def __init__(self, user_data):
        self.id = user_data.username
        self.password = user_data.password
        self.avatar = user_data.avatar
    
    """ Para obtener el usuario por su username """
    @staticmethod
    def get(username):
        user_data = get_user_by_username(username)
        return UserModel(user_data)