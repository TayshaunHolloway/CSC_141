people = [] 

person = {
    'first_name': 'Thomas',
    'last_name': 'Matthews',
    'age': 35,
    'city': 'Tusla',
    }
people.append(person)

person = {
    'first_name': 'Connor',
    'last_name': 'Matthews',
    'age': 2,
    'city': 'Tusla',
    }
people.append(person)

person = {
    'first_name': 'Lily',
    'last_name': 'Matthews',
    'age': 33,
    'city': 'Tusla',
    }
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()
    
    print(f"{name}, of {city}, is {age} years old.")
