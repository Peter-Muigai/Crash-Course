alien_0 = {'color': 'green', 'points': 5}

# Accessing Values in a Dictionary.
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

print("")
# Adding New Key-Value Pairs.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an empty dictionary.
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
print("")
# Modifying Values in a dictionary.
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.\n")

# Removing Key-Value pairs.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)