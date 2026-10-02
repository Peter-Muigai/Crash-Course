"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
•	Start with your program from Exercise 3-4. Add a print() call at the end
of your program stating the name of the guest who can’t make it.
•	Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
•	Print a second set of invitation messages, one for each person who is still
in your list.
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