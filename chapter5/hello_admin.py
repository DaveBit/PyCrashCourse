usernames = ['admin', 'david', 'james', 'lourdes', 'aitana', 'lorenz']

while True:
    name = str(input('Please insert your user name:'))
    if name.lower() in usernames:
        if name.lower() == 'admin':
            print('\nHello admin')
            print('\nWould you like to see a status report?')
            break
        else:
            print(f'Hello {name.title()}, thank you for logging in again')
            break
    else:
        print('User name is not valid')
