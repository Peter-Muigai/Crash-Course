from city_function import city_country

print("Enter 'q' anytime to quit.")
while True:
    city = input("Enter a city name: ")
    if city == 'q':
        break
    country = input("Enter the country the city is from: ")
    if country == 'q':
        break

    formatted_city = city_country(city, country)
    print(formatted_city)