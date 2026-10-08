"""
7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
"""
prompt = "\nPlease enter your age:"

while True:
    age = int(input(prompt))
    message = input("\nEnter 'quit' when you are finished.")

    if message == 'quit':
        break
    elif age < 3 and message != 'quit':
        price = 0
    elif 3 <= age <= 12 and message != 'quit':
        price = 10
    else:
        price = 15

    print(f"You will have to pay ${price} for your movie ticket.")