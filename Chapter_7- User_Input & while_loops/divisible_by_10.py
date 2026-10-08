"""
Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.
"""
number = int(input("Enter a number and I will tell if its divisible by 10: "))

if number % 10 == 0:
    print(f"\n{number} is a multiple of ten.")
else:
    print(f"\n{number} is not a multiple of ten.")