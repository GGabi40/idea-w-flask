from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from . import auth
from app.models import UserModel
from .forms import LoginForm, RegisterForm
from app.services import get_user_by_username


""" MÉTODO VISTA PARA LOGIN DE LOS USUARIOS """
@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    
    if login_form.validate_on_submit():
        user = get_user_by_username(login_form.username.data)
        if user is not None:
            if user.checkPassword(login_form.password.data):
                user_model = UserModel(user)
                login_user(user_model)
                flash('¡Bienvenido al Sistema de Ideas!', category='info')
                return redirect(url_for('ideas.home'))
            else:
                flash('Credenciales incorrectas...', category='error')
                pass
        else:
            flash('Credenciales incorrectas...', category='error')
            

    return render_template('auth/login.html', **context)


""" MÉTODO VISTA PARA REGISTER DE LOS USUARIOS """
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    register_form = RegisterForm()
    context = {
        'register_form': register_form
    }
    
    if register_form.validate_on_submit():
        pass

    return render_template('auth/signup.html', **context)