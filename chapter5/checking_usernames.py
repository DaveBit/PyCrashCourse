current_users = ['Admin', 'DavId', 'James', 'lourdes', 'aitana', 'lorenz']
new_users = ['Albert', 'Donte', 'Dayami', 'Jesse', 'Lailah']

current_users_lower = [user.lower() for user in current_users]
#  The above line is a compression of a for loop. See at the bottom the uncompressed way.

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'The user {new_user} is already in use. \nPlease, choose a different name')
    else:
        print(f'The user name {new_user} is available')

'''
current_user_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

Or as stated above:
current_users_lower = [user.lower() for user in current_users]
'''


