"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
"""
class Restaurant:
    """A simple class model representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant and cuisine type for restaurant."""
        self.name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a description for a restaurant."""
        print(f"\nRestaurant name: {self.name}")
        print(f"Cuisine type: {self.cuisine_type} cuisine")

    def open_restaurant(self):
        """Display a message showing restaurant is open."""
        print(f"{self.name} is open!")

my_restaurant = Restaurant('PeMu Place', 'French')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant('Cuisino', 'Italian')
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

their_restaurant = Restaurant('Palace', 'Spanish')
their_restaurant.describe_restaurant()
their_restaurant.open_restaurant()