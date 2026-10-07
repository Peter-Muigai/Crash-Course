"""
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.
"""
user_info = {'first_name': 'getrude', 'last_name': 'njeri', 'age': 55, 'city': 'nakuru'}

print(f"First name: {user_info['first_name'].title()}")
print(f"Last name : {user_info['last_name'].title()}")
print(f"Age: {user_info['age']}")
print(f"City of residence: {user_info['city'].title()}")