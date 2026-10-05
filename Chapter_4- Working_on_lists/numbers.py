# Making Numerical Lists
for value in range(1, 5):
    print(value)
print("\n")
for value in range(1, 6):
    print(value)
print("\n")

# Using range() to Make a List of Numbers
numbers = list(range(1, 6))
print(numbers)
print("\n")

# Printing even numbers between 1 and 10
even_numbers = list(range(2, 11, 2))
print(even_numbers)
print("\n")

# First 10 square numbers.
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)
print("\n")

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
print("\n")

# List Comprehensions
squares = [value ** 2 for value in range(1, 11)]
print(squares)