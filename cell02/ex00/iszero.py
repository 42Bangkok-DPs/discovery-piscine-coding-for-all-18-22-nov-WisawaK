try:
    number = float(input("Enter a number: "))
    if number == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except ValueError:
    print("Please enter a valid number.")
