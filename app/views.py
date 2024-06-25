from flask import request, jsonify
from app.models import Obra, Ruta, Categoria
from app.database import get_db

def index():
    response = {'message': 'Usando API-REST Flask!'}
    return jsonify(response)

def get_all_obras():
    obras = Obra.get_all()
    return jsonify([obra.serialize() for obra in obras])

def get_obra(id_obra):
    obra = Obra.get_by_id(id_obra)
    if obra is None:
        return jsonify({'error': 'Obra no encontrada'}), 404
    return jsonify(obra.serialize())

def validate_foreign_keys(ruta, categoria):
    return Ruta.exists(ruta) and Categoria.exists(categoria)

def create_obra():
    data = request.get_json()
    ruta = data.get('ruta')
    categoria = data.get('categoria')

    if not validate_foreign_keys(ruta, categoria):
        return jsonify({'error': 'Ruta o Categoria inválida'}), 400

    obra = Obra(**data)
    obra.insert()
    return jsonify(obra.serialize()), 201

def update_obra(id_obra):
    data = request.get_json()
    ruta = data.get('ruta')
    categoria = data.get('categoria')

    if not validate_foreign_keys(ruta, categoria):
        return jsonify({'error': 'Ruta o Categoria inválida'}), 400

    obra = Obra.get_by_id(id_obra)
    if obra is None:
        return jsonify({'error': 'Obra no encontrada'}), 404

    obra.update(data)
    return jsonify(obra.serialize()), 200

def delete_obra(id_obra):
    obra = Obra.get_by_id(id_obra)
    if obra is None:
        return jsonify({'error': 'Obra no encontrada'}), 404

    Obra.delete(id_obra)
    return jsonify({'message': 'Obra eliminada'}), 200

def get_all_rutas():
    rutas = Ruta.get_all()
    return jsonify([ruta.serialize() for ruta in rutas])

def get_all_categorias():
    categorias = Categoria.get_all()
    return jsonify([categoria.serialize() for categoria in categorias])