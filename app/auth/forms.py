from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length


""" Formulario de registro de usuario """
class RegisterForm(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired(), Length(min=2, max=20)])
    lastName = StringField("Apellido", validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField("Correo", validators=[DataRequired(), Email(), Length(min=5, max=30)])
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=10)])
    cellphone = StringField("Telefono", validators=[DataRequired(), Length(min=7, max=20)])
    password = PasswordField("Nueva Contraseña", validators=[DataRequired(), Length(min=6, max=10), EqualTo('password_confirm')])
    password_confirm = PasswordField("Confirmar Contraseña", validators=[DataRequired(), Length(min=6, max=10)])
    
    submit = SubmitField("Registrarme")


""" Formulario de Login """
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=10)])
    password = PasswordField("Ingrese Contraseña", validators=[DataRequired(), Length(min=6, max=10)])

    submit = SubmitField("Login")
    