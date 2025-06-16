from flask import Blueprint, jsonify, make_response
from server.models import db
from server.models.restaurant import Restaurant

bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')

@bp.route('', methods=['GET'])
def get_restaurants():
      restaurants = Restaurant.query.all()
      return jsonify([restaurant.to_dict() for restaurant in restaurants])

@bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
      restaurant = Restaurant.query.get(id)
      if not restaurant:
          return jsonify({'error': 'Restaurant not found'}), 404
      return jsonify(restaurant.to_dict())

@bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
      restaurant = Restaurant.query.get(id)
      if not restaurant:
          return jsonify({'error': 'Restaurant not found'}), 404
      db.session.delete(restaurant)
      db.session.commit()
      return make_response('', 204)