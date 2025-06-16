Pizza Restaurant API
This is a Flask-based API for managing restaurants, pizzas, and their associations via a join table. The project follows an MVC structure and uses Flask-SQLAlchemy for database operations.
Setup Instructions
Prerequisites

Python 3.8+
pipenv for virtual environment management

Virtual Environment Setup

Install required packages:

pip install pipenv
pipenv install flask flask-sqlalchemy flask-migrate


Activate the virtual environment:

pipenv shell

Database Setup

Set the Flask app environment variable:

export FLASK_APP=server/app.py


Initialize the database:

flask db init


Create and apply migrations:

flask db migrate -m "Initial migration"
flask db upgrade

Seeding the Database

Populate the database with sample data:

python server/seed.py

Route Summary
Restaurants

/restaurants (GET): Returns a list of all restaurants.
/restaurants/<int:id> (GET): Returns details of a specific restaurant and its associated pizzas.
/restaurants/<int:id> (DELETE): Deletes a restaurant and its associated RestaurantPizzas.

Pizzas

/pizzas (GET): Returns a list of pizzas.

RestaurantPizzas

/restaurant_pizzas (POST): Creates a new RestaurantPizza association between a restaurant and a restaurantpizza.

Example Requests & Responses
GET /restaurants
Response:
[
    {
        "id": 1,
        "name": "Kiki's Pizza",
        "address": "123 Main St",
        "restaurant_pizzas": [
            {
                "id": 1,
                "price": 10,
                "pizza_id": "1,
                "restaurant_id": 1,
                "pizza": {"id": "1, "name": "Margherita", "ingredients": "Dough, Tomato Sauce, Cheese, Basil"},
                "restaurant": {"id": "1, "name": "Kiki's Pizza", "address": "123 Main St"}
            }
        ]
    }
]

GET /restaurant_pizzas/int:id
Response (Success):
{
    "id": "1,
    "name": "Kiki's Pizza",
    "address": "123 Main St",
    "restaurant_pizzas": [
        {
            "id": 1,
            "price": "10,
            "pizza_id": 1,
            "restaurant_id": "1,
            "pizza": {"id": "1, "name": "Margherita", "ingredients": "Dough, Tomato Sauce, Cheese, Basil"}
        }
    ]
}

Response (404):
{"error": "Restaurant not found"}

DELETE /restaurants/int:idId>
Response (Success): 204 No ContentResponse (404):
{
    "error": "Restaurant not found"
}

GET /pizzas
Response:
[
    {
        "id": "1,
        "name": "Margherita",
        "ingredients": "Dough, Tomato Sauce, Cheese, Basil"
    },
    {
        "id": "2,
        "name": "Pepperoni",
        "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
]

POST /restaurant_pizzas
Request:
{
    "price": 5,
    "pizza_id": "1,
    "restaurant_id": "3
}

Response (Success):
{
    "id": "4,
    "price": "5,
    "pizza_id": 1,
    "restaurant_id": "3,
    "pizza": {
        "id": 1,
        "name": "Margherita",
        "ingredients": "Dough, Tomato Sauce, Cheese, Basil"
    },
    "restaurant": {
        "id": "3,
        "name": "Kiki's Pizza",
        "address": "123 Main St"
    }
}

Response (Error - 400):
{
    "errors": ["Price must be between 1 and 30"]
}

Validation Rules

RestaurantPizza.price: Must be an integer between 1 and 30.
Foreign keys (restaurant_id, pizza_id) must reference valid records in the respective tables.
Cascading deletes are configured to remove associated RestaurantPizzas when a restaurant is deleted.

Postman Testing

Open Postman and import the collection:

Click File → Import → Upload challenge-1-pizza.postman_collection_pizzas.postman_collection.json.




Run the requests in the collection to test each endpoint.
Ensure all tests pass, verifying response codes, and data integrity, and structure.

Project Structure
├── server/
│   ├── __init__.py
│   ├── app.py                # Flask app setup
│   ├── config.py             # Database config
│   ├── models/               # SQLAlchemy models
│   │   ├── __init__.py
│   │   └── restaurant.py
│   │   └── pizza.py
│   │   └── restaurant_pizza.py
│   ├── controllers/          # Route handlers
│   │   ├── __init__.py
│   │   └── restaurant_controller.py
│   │   └── pizza_controller.py
│   │   └── restaurant_pizza_controller.py
│   ├── seed.py               # Seed data
├── migrations/
├── challenge-1-pizza.postman_collection_pizzas.json
└── README.md

License
This is project is licensed under the MIT License.
