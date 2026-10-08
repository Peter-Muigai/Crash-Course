name = input("Please enter your name: ")
print(f"Hello, {name}!")

prompt = input("If you tell us who you are, we can personalize the message for you.")
prompt += "\nWhat's your name? "

name = input(prompt)
print(f"Hello, {name}")