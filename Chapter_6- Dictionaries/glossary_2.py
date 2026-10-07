"""
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When
you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.
"""

python_glossary = {
    'program': 'A set of instructions given to a computer.',
    'programming': 'It is giving a computer a set of instructions to execute.',
    'programmer': 'A person that writes computer programs.',
    'bugs': 'Refer to errors in a program.',
    'debug': 'Refers to fixing errors/bugs in a program.',
    }

print("---Python Glossary---")
for k, v in python_glossary.items():
    print(f"{k.title()}: {v} ")
print("\n")
python_glossary['immutable'] = 'A value that cannot change.'
python_glossary['list'] = 'A list is a collection of items in a particular order.'
python_glossary['tuple'] = 'Is an immutable list.'
python_glossary['set'] = 'A set is a collection in which each item must be unique.'
python_glossary['dictionary'] = 'A dictionary is a collection of key-value pairs.'

print("---Updated Python Glossary---")
for k, v in python_glossary.items():
    print(f"{k.title()}: {v}")