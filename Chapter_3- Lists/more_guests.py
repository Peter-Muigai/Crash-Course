"""
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
•	Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
call to the end of your program informing people that you found a bigger
dinner table.
•	Use insert() to add one new guest to the beginning of your list.
•	Use insert() to add one new guest to the middle of your list.
•	Use append() to add one new guest to the end of your list.
•	Print a new set of invitation messages, one for each person in your list
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