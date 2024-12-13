favorite_places = {
    'Devin': ['japan', 'new vegas', 'brazil'],
    'Michael': ['hawaii', 'iceland'],
    'Cindy': ['mt. fuji', 'canada', 'new hampshire']
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")