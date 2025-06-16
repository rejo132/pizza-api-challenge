from server.models import db

class Restaurant(db.Model):
      __tablename__ = 'restaurants'

      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String, nullable=False)
      address = db.Column(db.String, nullable=False)

      restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant', cascade='all, delete-orphan')

      def to_dict(self):
          return {
              'id': self.id,
              'name': self.name,
              'address': self.address,
              # Include only IDs of related restaurant_pizzas to avoid recursion
              'restaurant_pizzas': [rp.id for rp in self.restaurant_pizzas]
          }