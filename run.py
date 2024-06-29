from flask import Flask
from flask_cors import CORS
from app.views import *
from app.database import init_app

# Inicialización de app con Flask
app = Flask(__name__)

# Configurar CORS para todos los orígenes
CORS(app)

init_app(app)

# Rutas a atender con sus métodos asociados
app.route('/', methods=['GET'])(index)
app.route('/api/obras', methods=['GET'])(get_all_obras)
app.route('/api/obras', methods=['POST'])(create_obra)
app.route('/api/obras/<int:id_obra>', methods=['GET'])(get_obra)
app.route('/api/obras/<int:id_obra>', methods=['PUT'])(update_obra)
app.route('/api/obras/<int:id_obra>', methods=['DELETE'])(delete_obra)
app.route('/api/rutas', methods=['GET'])(get_all_rutas)
app.route('/api/categorias', methods=['GET'])(get_all_categorias)

if __name__ == '__main__':
    # Levanta servidor de desarrollo de Flask
    app.run(debug=True)