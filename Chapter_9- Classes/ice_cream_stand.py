"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
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

class IceCreamStand(Restaurant):
    """A simple class representing an Ice stand."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of Restaurant."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Chocolate", "Vanilla", "Strawberry", "Mint"]

    # overriding parent method
    def describe_restaurant(self):
        print(f"{self.name} is an Ice Cream Stand")

    def describe_flavors(self):
        print("Available flavors:")

        for flavor in self.flavors:
            print(f"- {flavor}")

my_stand = IceCreamStand('PeMu Stand', 'French')
my_stand.describe_restaurant()
my_stand.describe_flavors()
