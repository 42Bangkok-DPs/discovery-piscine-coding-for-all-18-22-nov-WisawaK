while True:
    user_input = input("What you gotta say? : ")
    if user_input.upper() == "STOP":
        print("I got that! Anything else? : STOP")
        break
    else:
        print(f"I got that! Anything else? : {user_input}")
