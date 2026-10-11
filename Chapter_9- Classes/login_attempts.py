"""
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 162). Write a method called increment_login
_attempts() that increments the value of login_attempts by 1. Write another
method called reset_login_attempts() that resets the value of login_attempts
to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""
class User:
    """A class representing a user."""

    def __init__(self, first_name, last_name, age, location):
        """Initialize user's attributes"""
        self.first = first_name
        self.last = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Display a description for a user."""
        print(f"\nFirst name: {self.first.title()}")
        print(f"Last name: {self.last.title()}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location.title()}")

    def greet_user(self):
        """Display a personalized greeting."""
        print(f"\nIt's nice to hear from you {self.first.title()}!")

    def read_login_attempts(self):
        """Display login attempts available."""
        print(f"You have {self.login_attempts} login attempts.")

    def increment_login_attempts(self):
        """Increment login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login attempts to 0."""
        self.login_attempts -= 1

my_profile = User('peter', 'muigai', 21, 'nyeri')
my_profile.describe_user()
my_profile.greet_user()
my_profile.increment_login_attempts()
my_profile.increment_login_attempts()
my_profile.reset_login_attempts()
my_profile.reset_login_attempts()
my_profile.read_login_attempts()