"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
"""
print("Good afternoon, welcome to PEmU INN")
prompt = "\nWhat toppings will you want on your pizza? "
choice = ''
while choice != 'quit':
    choice = input(prompt)
    if choice != 'quit':
        print(f"Adding {choice} to your pizza.")