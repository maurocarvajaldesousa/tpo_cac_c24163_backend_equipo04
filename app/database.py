import os
import mysql.connector
from flask import g, current_app
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Validar que todas las variables de entorno necesarias estén presentes.
# La variable DB_PASSWORD la omití para salvar excepción de password vacío
required_env_vars = ['DB_USERNAME', 'DB_HOST', 'DB_NAME']
for var in required_env_vars:
    if not os.getenv(var):
        raise EnvironmentError(f"Falta la variable de entorno necesaria: {var}")

DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': int(os.getenv('DB_PORT', 3306))  # puerto predeterminado es 3306 si no se especifica
}

# Función para obtener la conexión a la base de datos
def get_db():
    if 'db' not in g:
        try:
            g.db = mysql.connector.connect(**DATABASE_CONFIG)
        except mysql.connector.Error as err:
            current_app.logger.error(f"Error al conectar a la base de datos: {err}")
            raise
    return g.db

# Función para cerrar la conexión a la base de datos
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Función para inicializar la aplicación con el manejo de la base de datos
def init_app(app):
    app.teardown_appcontext(close_db)