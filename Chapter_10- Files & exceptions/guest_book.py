"""
10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
"""
filename = "guest_book.txt"

print("Welcome to the Guest Book!")
print("Enter 'q' at any time to quit.\n")

while True:
    name = input("Please enter your name: ")

    if name.lower() == 'q':
        print("Thank you for visiting!")
        break

    print(f"Hello, {name}! Welcome.")

    with open(filename, 'a') as file_object:
        file_object.write(name + '\n')