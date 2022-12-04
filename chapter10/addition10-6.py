try:
    number_one = int(input("Insert a number please.\n"))
    number_two = int(input("Insert a second number: \n"))
    final_number = int(number_one + number_two)
except ValueError:
    print("Something went wrong")
else:
    print("The final number is: " + str(final_number))
