"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.
"""
user_info_0 = {'first_name': 'getrude', 'last_name': 'njeri', 'age': 55, 'city': 'nakuru'}
user_info_1 = {'first_name': 'susan', 'last_name': 'wairimu', 'age': 48, 'city': 'kiambu'}
user_info_2 = {'first_name': 'neema', 'last_name': 'wanjiku', 'age': 12, 'city': 'kiambu'}

people = [user_info_0, user_info_1, user_info_2]
for person in people:
    print("\n")
    print(f"First name: {person['first_name'].title()}")
    print(f"Last name : {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City of residence: {person['city'].title()}")
