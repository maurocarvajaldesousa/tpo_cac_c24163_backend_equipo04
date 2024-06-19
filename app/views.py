from flask import Blueprint, jsonify
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