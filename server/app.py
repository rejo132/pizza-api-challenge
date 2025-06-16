from flask import Flask
from flask_migrate import Migrate
from server.config import Config
from server.models import db
from server.controllers.restaurant_controller import get_restaurants

app = Flask(__name__)
app.config.from_object(Config)

# Initialize db with app
db.init_app(app)
migrate = Migrate(app, db)

# Import models and controllers
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza
from server.controllers import restaurant_controller, pizza_controller, restaurant_pizza_controller

# Register blueprints
app.register_blueprint(restaurant_controller.bp)
app.register_blueprint(pizza_controller.bp)
app.register_blueprint(restaurant_pizza_controller.bp)

@app.route('/')
def home():
    return "Welcome to the Pizza API!"

@app.route('/restaurant', methods=['GET'])
def restaurant_alias():
    return get_restaurants()

if __name__ == '__main__':
    app.run(debug=True)