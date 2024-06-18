from flask import jsonify
from app.models import Obra

def index():
  response = {'message': 'Usando API-REST Flask!'}
  return jsonify(response)

# def get_all_obras():
#   response = {'message': 'Listar todas las obras!'}
#   return jsonify(response)

# def get_all_obras():
#   result_movies = Obra.get_all()
#   return jsonify(result_movies)
  
# def get_all_movies():
#     movies = Movie.get_all()
#     return jsonify([movie.serialize() for movie in movies])

def get_all_obras():
  obras = Obra.get_all()
  return jsonify([obra.serialize() for obra in obras])