from flask import jsonify

def index():
  response = {'message': 'Usando API-REST Flask!'}
  return jsonify(response)

def get_all_obras():
  response = {'message': 'Listar todas las obras!'}
  return jsonify(response)