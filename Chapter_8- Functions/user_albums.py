"""
8-8. User Albums: Start with your program from Exercise 8-7.
Write a while loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
"""
def make_album(name, title, number=None):
    """Display a dictionary of information about an album."""
    album = {'artist name': name.lower(), 'album name': title.lower()}
    if number:
        album['number'] = number
    return album

while True:
    print("\nEnter a musician and their album.")
    print("(enter 'q' at any time to quit)")
    a_name = input("Artist name: ")
    if a_name == 'q':
        break
    album_name = input("Album name: ")
    if album_name == 'q':
        break

    musician_album = make_album(a_name, album_name)
    print(musician_album)