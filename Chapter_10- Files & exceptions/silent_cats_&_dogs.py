"""
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
silently if either file is missing.
"""
def read_file(filename):
    """Reads content of a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    read_file(filename)