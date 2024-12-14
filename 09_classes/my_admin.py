from admin import Admin

tim = Admin('tim', 'connors', 't_connors', 't_connors@example.com', 'alaska')
tim.describe_user()

tim_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
tim.privileges.privileges = tim_privileges

print(f"\nThe admin {tim.username} has these privileges: ")
tim.privileges.show_privileges()