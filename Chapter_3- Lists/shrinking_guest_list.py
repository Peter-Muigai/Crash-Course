"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
•	Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
•	Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
•	Print a message to each of the two people still on your list, letting them
know they’re still invited.
•	Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
"""

guests = ['albert', 'stephen', 'sheldon', 'newton', 'eric']

invite = "I wish to invite you to dinner."

print("\n Invites: ")
print(f"{guests[0].title()}, {invite}")
print(f"{guests[1].title()}, {invite}")
print(f"{guests[2].title()}, {invite}")
print(f"{guests[3].title()}, {invite}")
print(f"{guests[4].title()}, {invite}")

print(f"\n{guests[2].title()} has canceled invite and won't be available")

guests = ['albert', 'stephen', 'mark', 'newton', 'eric']
print("\n", guests)

print("\n Modified invites: ")
print(f"{guests[0].title()}, {invite}")
print(f"{guests[1].title()}, {invite}")
print(f"{guests[2].title()}, {invite}")
print(f"{guests[3].title()}, {invite}")
print(f"{guests[4].title()}, {invite}")

print("\nI have found a bigger table for us and will invite more guests.")

guests.insert(0, 'sharon')
guests.insert(2, 'kim')
guests.append('nick')

print(guests)
print("\n Modified invites: ")
print(f"{guests[0].title()}, {invite}")
print(f"{guests[1].title()}, {invite}")
print(f"{guests[2].title()}, {invite}")
print(f"{guests[3].title()}, {invite}")
print(f"{guests[4].title()}, {invite}")
print(f"{guests[5].title()}, {invite}")
print(f"{guests[6].title()}, {invite}")
print(f"{guests[7].title()}, {invite}")

print("\nI just found out that the table won't arrive in time and can only invite two.")

first_cancel = guests.pop()
print(f"{first_cancel.title()},I am very sorry I can't invite you to dinner.")

second_cancel = guests.pop()
print(f"{second_cancel.title()},I am very sorry I can't invite you to dinner.")

third_cancel = guests.pop()
print(f"{third_cancel.title()},I am very sorry I can't invite you to dinner.")

fourth_cancel = guests.pop()
print(f"{fourth_cancel.title()},I am very sorry I can't invite you to dinner.")

fifth_cancel = guests.pop()
print(f"{fifth_cancel.title()},I am very sorry I can't invite you to dinner.")

sixth_cancel = guests.pop()
print(f"{sixth_cancel.title()},I am very sorry I can't invite you to dinner.")

print("\nModified Invite list:")
print(f"{guests[0].title()}, {invite}")
print(f"{guests[1].title()}, {invite}")

del guests[0]
del guests[0]
print("\n")
print(guests)