from random import randint

operation = {
    "+": "addition",
    "-": "subtraction",
    "*": "multiplication"
}

def addition():
    a = randint(10,100)
    b = randint(10,100)
    result = a + b
    user_input = int(input(f"Enter the answer\n {a} + {b} : "))
    if result == user_input:
        print("Congratulations, Your answer is correct ✅")
    else:
        print(f"Your answer is incorrect ❌.\nCorrect answer is: {result}")

def subtraction():
    a = randint(10,100)
    b = randint(10,100)
    result = a - b
    user_input = int(input(f"Enter the answer\n {a} - {b} : "))
    if result == user_input:
        print("Congratulations, Your answer is correct ✅")
    else:
        print(f"Your answer is incorrect ❌.\nCorrect answer is: {result}")

def multiplication():
    a = randint(10,100)
    b = randint(10,100)
    result = a * b
    user_input = int(input(f"Enter the answer\n {a} * {b} : "))
    if result == user_input:
        print("Congratulations, Your answer is correct ✅")
    else:
        print(f"Your answer is incorrect ❌.\nCorrect answer is: {result}")

# ---- Main Program ----
user_choice = input(f"Enter the calculation method {list(operation.keys())}: ")
n = int(input("How many questions do you want to practice? : "))

def calculation():
    for i in range(n):
        if user_choice == "+":
            addition()
        elif user_choice == "-":
            subtraction()
        elif user_choice == "*":
            multiplication()
        else:
            print("Invalid choice ❌")
            break
    
    print("Thank you for practicing! 🎉")

# Call the function
calculation()
