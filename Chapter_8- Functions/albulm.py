"""
8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album.
"""
def make_album(name, title):
    """Display a dictionary of information about an album."""
    album = {'artist name': name, 'album name': title}
    return album

music = make_album('post malone', 'f trillion')
print(music)

music = make_album('taylor swift', 'love')
print(music)

music = make_album('doja cat', 'like that')
print(music)

# Modified function
def make_album(name, title, number=None):
    """Display a dictionary of information about an album."""
    album = {'artist name': name, 'album name': title}
    if number:
        album['number'] = number
    return album

music = make_album('marron 5', 'sugar', 12)
print(music)