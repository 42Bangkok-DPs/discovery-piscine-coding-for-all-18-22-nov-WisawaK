# isneg.py

def main():
    # Prompt the user to enter a number
    try:
        number = float(input("Please enter a number: "))
        
        # Determine if the number is positive, negative, or zero
        if number > 0:
            print("This number is positive.")
        elif number < 0:
            print("This number is negative.")
        else:
            print("This number is both positive and negative.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
