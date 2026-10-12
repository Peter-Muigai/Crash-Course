"""
10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
"""
filename = 'programming_poll.txt'
print(" I will be conducting a poll for why you love Python.")
print("Enter 'q' anytime to quit.")

while True:
    reason = input("Why do you love python? ")

    if reason .lower() == 'q':
        print("Thank you for participating!")
        break

    with open(filename, 'a') as file_object:
        file_object.write(reason + "\n")