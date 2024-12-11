usernames = ['taylin', 'jen', 'admin', 'bryan', 'evan']

for username in usernames:
    if username == 'Admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for loggin in again!")

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for loggin in again!")
else:
    print("We need to find some users!")