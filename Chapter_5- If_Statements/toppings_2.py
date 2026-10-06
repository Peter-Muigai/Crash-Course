requested_toppings = ['mushroom', 'extra cheese', 'green peppers']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza.")
print("\n")

# Handling an item in list using if-else.
requested_toppings = ['mushroom', 'extra cheese', 'green peppers']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green papers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza.")
