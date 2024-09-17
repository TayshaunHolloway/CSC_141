# Review of everything I learned
names = ['Tyson','Pablo','Aaron','Cassandra','Max']
print (names[0])
message = f"{names[1]} is an extrovert."
print(message)

names.append('Ally')
print(names)

del names[2]
print(names)

popped_names = names.pop()
print(names)
print(popped_names)

names.sort()
print(names)

names.sort(reverse=True)
print(names)

print("Here's the original list")
print(names)

print("\nhere's the sorted list")
print(sorted(names))

print("\nHere's the original list")
print(names)

names.reverse()
print(names)

num_of_names = len(names)
print(names)
print(num_of_names)