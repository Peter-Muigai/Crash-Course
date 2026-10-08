"""
7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message say
ing they’ll have to wait for a table. Otherwise, report that their table is ready.
"""
prompt = input("Good evening, and how many people are in your dinner group? ")
prompt = int(prompt)

if prompt >= 8:
    print("\nAm very sorry, you'll have to wait for a table.")
else:
    print("\nYour table is ready, right this way.")