# Return Values.
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('doja', 'cat')
print(musician)

# Making arguments optional.
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"\n{first_name} {middle_name} {last_name}"
    else:
        full_name =f"\n{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('billy', 'bob', 'cyrus')
print(musician)
musician = get_formatted_name('annie', 'marie')
print(musician)