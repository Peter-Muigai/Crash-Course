"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any num
ber you like that could represent how many customers were served in, say, a
day of business.
"""

class Restaurant:
    """A simple class model representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant and cuisine type for restaurant."""
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """Display a description for a restaurant."""
        print(f"Restaurant name: {self.name}")
        print(f"Cuisine type: {self.cuisine_type} cuisine")

    def open_restaurant(self):
        """Display a message showing restaurant is open."""
        print(f"{self.name} is open!")

    def read_number_served(self):
        """Displays the number served."""
        print(f"The number served today is {self.number_served}.")

    def set_number_served(self, number):
        """Set the number served to a given value."""
        self.number_served = number

    def increment_number_served(self, served):
        """Increment number served."""
        self.number_served += served

my_restaurant = Restaurant('PeMu Place', 'French')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(8)
my_restaurant.increment_number_served(3)
my_restaurant.read_number_served()