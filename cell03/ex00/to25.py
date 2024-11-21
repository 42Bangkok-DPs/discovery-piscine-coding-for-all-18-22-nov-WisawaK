try:
    user_input = int(input("Enter a number less than 25: "))
except ValueError:
    print("Invalid input. Please enter a numeric value.")
    exit()
if user_input > 25:
    print("Error")
else:
    for i in range(user_input, 26):
        print(f"Inside the loop, my variable is {i}")
