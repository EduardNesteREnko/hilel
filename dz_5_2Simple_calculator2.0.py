while True:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    action = input("Action: ")

    if action == "+":
        print("Result:", a + b)
    elif action == "-":
        print("Result:", a - b)
    elif action == "*":
        print("Result:", a * b)
    elif action == "/":
        if b == 0:
            print("Zero is not allowed")
        else:
            print("Result:", a / b)
    else:
        print("Unknown action!")

    cont = input("Continue? (y/yes to continue): ")
    if cont != "y" and cont != "yes":
        print("Goodbye!")
        break
