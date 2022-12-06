while True:
    try:
        x = input("Insert a number please.\n")
        if x == 'q':
            break
        number_one = int(x)

        y = input("Insert a second number: \n")
        if y == 'q':
            break
        number_two = int(y)

    except ValueError:
        print("Something went wrong\n Let's start again")

    else:
        final_number = x + y
        print("The final number is: " + str(final_number))
