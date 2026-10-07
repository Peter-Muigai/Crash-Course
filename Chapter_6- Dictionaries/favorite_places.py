"""
6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places.
"""
favorite_places ={
    'kim': ['paris', 'egypt'],
    'joy': ['new york', 'canada', 'india'],
    'paul': ['nairobi']
    }

for name, places in favorite_places.items():
    if len(places) != 1:
        print(f"\n{name.title()}'s favorite places are:")
        for place in places:
            print(f"\t{place.title()}")
    else:
        print(f"\n{name.title()}'s favorite place is:")
        for place in places:
            print(f"\t{place.title()}")