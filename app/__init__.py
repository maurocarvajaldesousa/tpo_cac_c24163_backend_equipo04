from flask import Flask
from app.database import init_app
from app.views import bp as main_bp

def create_app():
    app = Flask(__name__)
    
    # Inicializar la base de datos
    init_app(app)
    
    # Registrar Blueprint
    app.register_blueprint(main_bp)
    
    return app