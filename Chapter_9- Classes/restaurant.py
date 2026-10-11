"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message
indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two
attributes individually, and then call both methods.
"""
class Restaurant:
    """A simple class model representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant and cuisine type for restaurant."""
        self.name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a description for a restaurant."""
        print(f"Restaurant name: {self.name}")
        print(f"Cuisine type: {self.cuisine_type} cuisine")

    def open_restaurant(self):
        """Display a message showing restaurant is open."""
        print(f"{self.name} is open!")

my_restaurant = Restaurant('PeMu Place', 'French')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()