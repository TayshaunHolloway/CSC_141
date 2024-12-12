pets = []

pet = {
    'animal type': 'Dog',
    'name': 'Dexter',
    'owner': 'Johnny',
    'weight': 20,
    'eats': 'bones',
}
pets.append(pet)

pet = {
    'animal type': 'Spider',
    'name': 'Charlotte',
    'owner': 'Tiffany',
    'weight': 3,
    'eats': 'Bugs',
}
pets.append(pet)

pet = {
    'animal type': 'Cat',
    'name': 'Ray',
    'owner': 'Eric',
    'weight': 12,
    'eats': 'Mice',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")