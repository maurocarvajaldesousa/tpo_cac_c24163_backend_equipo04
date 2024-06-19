from flask import Blueprint, jsonify, request, abort
from app.models import Obra

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    response = {'message': 'Usando API-REST Flask!'}
    return jsonify(response)

@bp.route('/api/obras', methods=['GET'])
def get_all_obras():
    obras = Obra.get_all()
    return jsonify([obra.serialize() for obra in obras])

@bp.route('/api/obras/<int:id_obra>', methods=['GET'])
def get_obra(id_obra):
    obra = Obra.get_by_id(id_obra)
    if obra is None:
        abort(404)
    return jsonify(obra.serialize())

@bp.route('/api/obras', methods=['POST'])
def create_obra():
    data = request.get_json()
    obra = Obra(
        descripcion=data.get('descripcion'),
        anio=data.get('anio'),
        partido=data.get('partido'),
        localidad=data.get('localidad'),
        latitud=data.get('latitud'),
        longitud=data.get('longitud'),
        gmaps=data.get('gmaps'),
        imagen=data.get('imagen'),
        ruta=data.get('ruta'),
        categoria=data.get('categoria'),
        estado=data.get('estado')
    )
    obra.save()
    return jsonify(obra.serialize()), 201

@bp.route('/api/obras/<int:id_obra>', methods=['PUT'])
def update_obra(id_obra):
    obra = Obra.get_by_id(id_obra)
    if obra is None:
        abort(404)
    
    data = request.get_json()
    obra.descripcion = data.get('descripcion', obra.descripcion)
    obra.anio = data.get('anio', obra.anio)
    obra.partido = data.get('partido', obra.partido)
    obra.localidad = data.get('localidad', obra.localidad)
    obra.latitud = data.get('latitud', obra.latitud)
    obra.longitud = data.get('longitud', obra.longitud)
    obra.gmaps = data.get('gmaps', obra.gmaps)
    obra.imagen = data.get('imagen', obra.imagen)
    obra.ruta = data.get('ruta', obra.ruta)
    obra.categoria = data.get('categoria', obra.categoria)
    obra.estado = data.get('estado', obra.estado)
    obra.save()
    return jsonify(obra.serialize())

@bp.route('/api/obras/<int:id_obra>', methods=['DELETE'])
def delete_obra(id_obra):
    obra = Obra.get_by_id(id_obra)
    if obra is None:
        abort(404)
    obra.delete()
    return '', 204