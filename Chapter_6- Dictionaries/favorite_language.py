# A Dictionary of Similar Objects.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.\n")

# Looping Through All Key-Value Pairs
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")
# Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
    print(name.title())
print("\n")
# Friends in dictionary.
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!\n")

# Looping Through a Dictionary’s Keys in a Particular Order.
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
print("\n")

# Looping Through All Values in a Dictionary.
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
