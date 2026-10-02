# Modifying elements in a list.
motorcycles = ['honda', 'suzuki', 'yamaha', 'boxer']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# Appending an element into a list.
motorcycles.append('isuzu')
print(motorcycles)


motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Inserting Elements into a List
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing elements from a list
motorcycles = ['ducati', 'honda', 'yamaha']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# Removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# Using popped item
motorcycles = ['yamaha', 'honda', 'suzuki']
last_owned = motorcycles.pop()
print(f"The motorcycle I owned last was a {last_owned.title()}.")

# Popping Items from any Position in a List
first_owned = motorcycles.pop(0)
print(f"\nThe motorcycle I owned first was a {first_owned.title()}.")

# Removing an Item by Value
motorcycles = ['yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

# Work with a removed item
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

