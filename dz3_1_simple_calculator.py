a = int(input("First number: "))
b = int(input("Second number: "))
action = input("Action: ")

if action == "+":
    print(a + b)
elif action == "-":
    print(a - b)
elif action == "*":
    print(a * b)
elif action == "/":
    if b != 0:
        print(a / b)
    else:
        print("Zero is not allowed")
else:
    print("Unknown action!")
