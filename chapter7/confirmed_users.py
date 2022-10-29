unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    confirmed_users.append(unconfirmed_users.pop())

print(unconfirmed_users)
print(confirmed_users)

list1 = [1, 2, 3, 5, 6, 6, 7, 8, 6, 5, 4]
list1 = list(set(list1))
print(list1)
