"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
"""
class User:
    """A class representing a user."""

    def __init__(self, first_name, last_name, age, location):
        """Initialize user's attributes"""
        self.first = first_name
        self.last = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        """Display a description for a user."""
        print(f"\nFirst name: {self.first.title()}")
        print(f"Last name: {self.last.title()}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location.title()}")

    def greet_user(self):
        """Display a personalized greeting."""
        print(f"\nIt's nice to hear from you {self.first.title()}!")

my_profile = User('peter', 'muigai', 21, 'nyeri')
my_profile.describe_user()
my_profile.greet_user()

my_friend = User('john', 'mwai', 24, 'nairobi')
my_friend.describe_user()
my_friend.greet_user()