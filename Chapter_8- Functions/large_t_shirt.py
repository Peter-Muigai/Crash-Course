"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""
def make_shirt(size='large', text='i love python'):
    """Display a T-shirt."""
    print(f"A {size} T-Shirt with {text.title()} written on it.")

make_shirt('large', 'i love python')
make_shirt('medium', 'i love python')
make_shirt(size='small', text='family guy')