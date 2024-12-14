prompt = "\nwhat would you like to buy?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    item = input(prompt)
    if item != 'quit':
        print(f"  I'll get the {item} for you.")
    else:
        break