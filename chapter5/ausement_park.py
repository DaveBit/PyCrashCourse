age = int(input("What's your age?"))
if age < 4:
    price = 4
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")
