from app import create_app
from app.migrate import init_db

from flask import render_template

app = create_app()


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/database')
def database():
    init_db()
    return "Base de datos creada correctamente."


if __name__ == '__main__':
    app.run(debug=True)