from flask import render_template
from flask_login import login_required
from . import ideas


""" Método para retornar al home de la app """
@ideas.route('/home')
@login_required
def home():
    return render_template('ideas/home.html')