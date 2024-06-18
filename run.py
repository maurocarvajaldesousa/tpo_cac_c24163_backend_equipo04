from flask import Flask
from app.views import *

# inicialización de app con Flask
app = Flask(__name__)

# rutas a atender con sus métodos asociados
app.route('/', methods=['GET']) (index)
app.route('/api/obras', methods=['GET']) (get_all_obras)

if (__name__ == '__main__'):
  # levanta server de desarrollo de Flask
  app.run(debug = True)