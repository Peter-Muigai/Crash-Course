"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99)
so each person can have more than one favorite number. Then print each per
son’s name along with their favorite numbers.
"""
favorite_numbers = {
    'peter': [7, 2, 4],
    'sharon': [2, 34, 78],
    'mark': [4, 99],
    'john': [9, 77, 132, 512],
    'kevin': [5],
    }

for person, numbers in favorite_numbers.items():
    if len(numbers) != 1:
        print(f"{person.title()}'s favorite numbers are:")
        for number in numbers:
            print(f"\t{number}")
    else:
        print(f"{person.title()}'s favorite number is:")
        for number in numbers:
            print(f"{number}")