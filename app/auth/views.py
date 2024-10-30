from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from . import auth
from app.models import UserModel
from .forms import LoginForm, RegisterForm


""" MÉTODO VISTA PARA LOGIN DE LOS USUARIOS """
@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    
    if login_form.validate_on_submit():
        pass

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