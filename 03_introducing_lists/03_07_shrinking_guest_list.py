# Shrinking list size to only two guest
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
print(f'Unfortunatly, only two people can be invited.')

Guest1 = guest_list.pop(0)
print(f"Sorry {Guest1}, unfortunatly you've been removed off the list.")
Guest4 = guest_list.pop(2)
print(f"Sorry {Guest4}, unfortunatly you've been removed off the list.")
Guest6 = guest_list.pop(3)
print(f"Sorry {Guest6}, unfortunatly you've been removed off the list.")
Guest3 = guest_list.pop(1)
print(f"Sorry {Guest3}, unfortunatly you've been removed off the list.")
new_message = f"{guest_list[0]}, you're still invited to dinner."
print(new_message)
new_message = f"{guest_list[1]}, you're still invited to dinner."
print(new_message)

del guest_list[1]

del guest_list[0]
print(guest_list)
print(f'Guest list is fully erased.')
