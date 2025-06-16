from flask import Blueprint, jsonify, request
from server.models import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

bp = Blueprint('restaurant_pizzas', __name__, url_prefix='/restaurant_pizzas')

@bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        price = data['price']
        pizza_id = data['pizza_id']
        restaurant_id = data['restaurant_id']

        # Validate restaurant and pizza exist
        restaurant = Restaurant.query.get(restaurant_id)
        pizza = Pizza.query.get(pizza_id)
        if not restaurant or not pizza:
            return jsonify({'errors': ['Restaurant or Pizza not found']}), 404

        # Create new RestaurantPizza
        restaurant_pizza = RestaurantPizza(
            price=price,
            pizza_id=pizza_id,
            restaurant_id=restaurant_id
        )
        db.session.add(restaurant_pizza)
        db.session.commit()

        return jsonify(restaurant_pizza.to_dict()), 201
    except ValueError as e:
        return jsonify({'errors': [str(e)]}), 400
    except Exception as e:
        return jsonify({'errors': ['Invalid data']}), 400