from app import create_app
from app.migrate import init_db

from flask import render_template, flash

app = create_app()



@app.route('/')
def index():
    flash("¡Este es un mensaje de prueba!", category='error')
    return render_template('index.html')



@app.route('/database')
def database():
    init_db()
    return "Base de datos creada correctamente."


""" Método para manejar errores 404 """
@app.errorhandler(404)
def not_found(error):
    return render_template('errors/error404.html', error=error)


""" Método para manejar errores 500 """
@app.errorhandler(500)
def internal_server_error():
    return render_template('errors/error500.html')



if __name__ == '__main__':
    app.run(debug=True)