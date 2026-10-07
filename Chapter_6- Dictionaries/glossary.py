"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
•	Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
•	Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.
"""
python_glossary = {
    'program': 'A set of instructions given to a computer.',
    'programming': 'It is giving a computer a set of instructions to execute.',
    'programmer': 'A person that writes computer programs.',
    'bugs': 'Refer to errors in a program.',
    'debug': 'Refers to fixing errors/bugs in a program.',
    }

print("---Python Glossary---")
print(f"Program: {python_glossary['program']}\n")
print(f"Programming: {python_glossary['programming']}\n")
print(f"Programmer: {python_glossary['programmer']}\n")
print(f"Bugs: {python_glossary['bugs']}\n")
print(f"Debug: {python_glossary['debug']}")