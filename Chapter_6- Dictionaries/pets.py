"""
6-8. Pets: Make several dictionaries, where each dictionary represents a
different pet. In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet.
"""
pet_0 = {'owner': 'mark', 'kind': 'dog', 'name': 'max'}
pet_1 = {'owner': 'peter', 'kind': 'cat', 'name': 'tommy'}
pet_2 = {'owner': 'sharon', 'kind': 'parrot', 'name': 'cracker'}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"\n{pet['owner'].title()} has a  {pet['kind']} for a pet named {pet['name'].title()}.")