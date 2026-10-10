# Default values.
def describe_pets(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pets(pet_name='willie')
describe_pets(pet_name='max')
describe_pets('pike')
describe_pets('harry', animal_type='hamster')