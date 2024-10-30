# Cada dependencia de requirements.txt:
## flask
Marco principal de la app.

## flask-bootstrap
Integra bootstrap en Flask (facilita diseño).

## flask-wtf
Simplifica manejo de formularios con validacion y protección CSRF.

## flask-testing
Herramientas para prueba unitarias en app Flask.

## flask-sqlalchemy
Conecta Flask con SQLAlchemy (facilita manejo de datos). Utilizado principalmente en database.py

    DOCS: https://flask-sqlalchemy.readthedocs.io/en/stable/models/

## flask-login
Gestiona la autenticación y sesiones de manera segura.

## flask-FontAwesome
Íconos de Font Awesome.

## marshmallow-sqlalchemy
Facilita serialización y deserialización de datos.

## email-validator
Valida direcciones de correo electrónico, asegura que emails sean válidos.


---------------------
# Instalar extensión (VsCode)
## SQLite 
_(Opcional)_
Permite ver los archivos .db en forma de tabla


_(Me descargué DBeaver para ver las tablas)_

---------------------

# Estructura de un Proyecto con Flask

### main.py
Este es el punto de entrada de la aplicación Flask. En él se crea la instancia de la app y se definen las rutas.

### __init_.py
Fundamental en aplicaciones Flask. Su función principal es crear la instancia de la aplicación y configurar la misma. Además, se pueden inicializar extensiones y registrar blueprints.

### Rutas
Las rutas en Flask se definen utilizando decoradores sobre funciones que manejan solicitudes HTTP.

Ejemplo: 

    @app.route('/')
    def index():
        return render_template('index.html')

---------------------
# Carpetas Importantes:
## Src o App
Es el núcleo de tu aplicación Flask. Aquí es donde resides el código fuente de la aplicación, organizando los módulos, paquetes y recursos necesarios para su funcionamiento.
La estructura típica de la carpeta incluye:

    __init__.py: inicializar el paquete de la aplicación. Se crea la instancia de Flask, se configuran extensiones, se registran blueprints y se define la estructura de la aplicación.

    config.py: Contiene la configuración de la aplicación, como claves secretas, configuraciones de la base de datos y otras variables de entorno.

    database.py: Maneja la conexión y operaciones relacionadas con la base de datos. Aquí puedes definir el modelo de datos utilizando SQLAlchemy y manejar la creación de tablas.

    models.py: Define los modelos de datos que representan las tablas en la base de datos. Se utiliza SQLAlchemy para definir las clases que corresponden a las tablas.

    routes.py: Contiene las rutas de la aplicación, es decir, las URL y las funciones que se ejecutan cuando se accede a esas URL.

    views.py: Define las vistas que se renderizan para cada ruta. A menudo se utiliza para agrupar la lógica de las vistas relacionadas.

    auth/: Una carpeta que contiene el blueprint para autenticación, que a su vez puede incluir su propio __init__.py y views.py, además de cualquier otro archivo relacionado.

    tamplates/: Carpeta que contiene las plantillas HTML utilizadas para renderizar las vistas de la aplicación (JINJA).

    static/:  Carpeta que alberga archivos estáticos como CSS, JavaScript e imágenes. Aquí se colocan los recursos que no cambian y se sirven directamente al cliente.

## Templates
Es crucial en un proyecto Flask, ya que es donde se almacenan las plantillas HTML que se utilizan para renderizar las vistas.

Plantilla Base: Muchas aplicaciones incluyen una plantilla base (como base.html) que define la estructura común de todas las páginas (como encabezados, pies de página y menús de navegación).

Templates Específicos:  Puedes tener múltiples archivos de plantilla (por ejemplo, index.html, login.html, profile.html) que contienen el HTML específico para cada vista.

Uso de bloques: Jinja2 permite definir bloques en las plantillas, lo que facilita la reutilización de código. Por ejemplo, puedes definir un bloque content en tu plantilla base y luego llenarlo con contenido específico en tus plantillas extendidas.

---------------------
# Jerarquía de Carpetas:
## Se recomienda:

    /proyecto/
    │
    ├── app/ (o src/)             # Carpeta principal de la aplicación
    │   ├── __init__.py           # Inicialización de la app
    │   ├── config.py             # Configuración de la aplicación
    │   ├── database.py           # Manejo de la base de datos
    │   ├── models.py             # Definición de modelos de datos
    │   ├── routes.py             # Rutas de la aplicación
    │   ├── views.py              # Vistas de la aplicación
    │   ├── auth/                 # Blueprint para autenticación
    │   │   ├── __init__.py       # Inicialización del blueprint
    │   │   ├── views.py          # Vistas de autenticación
    │   ├── templates/            # Plantillas HTML
    │   │   ├── base.html         # Plantilla base
    │   │   ├── index.html        # Plantilla de la página principal
    │   │   ├── navbar.html       # Plantilla de navegación
    │   ├── static/               # Archivos estáticos (CSS, JS, imágenes)
    │   │   ├── css/              # Archivos CSS
    │   │   ├── js/               # Archivos JavaScript
    │   │   ├── img/              # Imágenes
    │
    ├── main.py                   # Punto de entrada de la aplicación
    ├── requirements.txt          # Dependencias del proyecto
    └── README.md                 # Documentación del proyecto
