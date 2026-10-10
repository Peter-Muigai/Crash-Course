"""
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
Call your function with at least three city-country pairs, and print the
values that are returned.
"""
def city_country(name, country):
    """Display a formatted city and its country."""
    formatted_name = f"{name.title()}, {country.title()}"
    return formatted_name

city = city_country('nairobi', 'kenya')
print(city)

city = city_country('ney york', 'america')
print(city)

city = city_country('montreal', 'canada')
print(city)