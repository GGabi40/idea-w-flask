from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')

from . import views

""" EN ESTE ARCHIVO:
Organiza la app en módulos.

La clase Blueprint de Flask permite crear módulos dentro de una app Flask.
Es útil para dividir la app en componentes reutilizables.

auth = Blueprint() -> referencia el blueprint de la app.


auth = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')

'auth' -> Nombre del Blueprint, se utilizará en rutas

__name__  ->  Ayuda flask a encontrar recursos relativos a este módulo. Pueden
        ser archivos de plantilla y archivos estáticos.
        
url_prefix='/auth' -> Prefijo que agregará todas las rutas definidas en el blueprint.
            Por ejemplo, si hay una ruta /login la ruta completa será /auth/login

template_folder='templates'  ->  Especifica directorio donde se encuentran las 
                    plantillas HTML que se utilizarán con este blueprint.


from . import views -> importa módulo views (maneja mejor las rutas asociadas al blueprint)
"""