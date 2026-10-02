# Sorting a List Permanently with the sort() Method.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Sorting in reverse alphabetical order.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\n")
print(cars)
cars.reverse()
print(cars)
# Finding the Length of a List
print(len(cars))