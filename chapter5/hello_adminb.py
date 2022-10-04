usernames = ['admin', 'david', 'james', 'lourdes', 'aitana', 'lorenz']

for username in usernames:
    if username.lower() == 'admin':
        print('Hello admin. Would you like to see a status report?')
    else:
        print(f'hello {username.title()}, thanks your for logging in again!')

