"""
10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
"""
print("Welcome!")
name = input("Can I have your name please: ")

filename = 'guests.txt'
with open(filename, 'w')as file_object:
    file_object.write(name)