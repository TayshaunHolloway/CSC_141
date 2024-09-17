# Adding people to the list
guest_list = ['Gabriel Iglesias', 'Billy Kametz', "Akira Toriyama"] 
letter = f"Congrats {guest_list[0]}, you've been invited to a dinner with yours truly."
print (letter)
letter = f"Congrats {guest_list[1]}, you've been invited to a dinner with yours truly."
print (letter)
letter = f"Congrats {guest_list[2]}, you've been invited to a dinner with yours truly."
print (letter)
print (f'Remove one guest from the list')

guest_list[0] = 'Evan Fong'
letter = f"Congrats {guest_list[0]}, you've been invited to a dinner with yours truly."
print (letter)
letter = f"Congrats {guest_list[1]}, you've been invited to a dinner with yours truly."
print(letter)
letter = f"Congrats {guest_list[2]}, you've been invited to a dinner with yours truly."
print(letter)
print(f'Able to add three people to the list.')

guest_list.insert(0, 'Sonny Strait')
guest_list.insert(2, 'Chadwick Boseman')
guest_list.insert(3, 'Nathan Feuerstien')
letter = f"Congrats {guest_list[0]}, you've been invited to a dinner with yours truly."
print(letter)
letter = f"Congrats {guest_list[1]}, you've been invited to a dinner with yours truly."
print(letter)
letter = f"Congrats {guest_list[2]}, you've been invited to a dinner with yours truly."
print(letter)
letter = f"Congrats {guest_list[3]}, you've been invited to a dinner with yours truly."
print(letter)
letter = f"Congrats {guest_list[4]}, you've been invited to a dinner with yours truly."
print(letter)
letter = f"Congrats {guest_list[5]}, you've been invited to a dinner with yours truly."
print(letter)