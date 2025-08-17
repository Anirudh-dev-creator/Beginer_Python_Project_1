from random import randint, choice

operation = {
    "+": "addition",
    "-": "subtraction",
    "*": "multiplication",
    "random": "mix of + - *"
}

def addition():
    a = randint(10,100)
    b = randint(10,100)
    result = a + b
    user_input = int(input(f"Enter the answer\n {a} + {b} : "))
    if result == user_input:
        print("Congratulations, Your answer is correct ✅")
        return True
    else:
        print(f"Your answer is incorrect ❌.\nCorrect answer is: {result}")
        return False

def subtraction():
    a = randint(10,100)
    b = randint(10,100)
    result = a - b
    user_input = int(input(f"Enter the answer\n {a} - {b} : "))
    if result == user_input:
        print("Congratulations, Your answer is correct ✅")
        return True
    else:
        print(f"Your answer is incorrect ❌.\nCorrect answer is: {result}")
        return False

def multiplication():
    a = randint(10,100)
    b = randint(10,100)
    result = a * b
    user_input = int(input(f"Enter the answer\n {a} * {b} : "))
    if result == user_input:
        print("Congratulations, Your answer is correct ✅")
        return True
    else:
        print(f"Your answer is incorrect ❌.\nCorrect answer is: {result}")
        return False

# ---- Main Program ----
user_choice = input(f"Enter the calculation method {list(operation.keys())}: ")
n = int(input("How many questions do you want to practice? : "))

def calculation():
    score = 0
    for i in range(n):
        # If random mode, pick one operator at random
        current_choice = user_choice
        if user_choice == "random":
            current_choice = choice(["+", "-", "*"])

        if current_choice == "+":
            if addition():
                score += 1
        elif current_choice == "-":
            if subtraction():
                score += 1
        elif current_choice == "*":
            if multiplication():
                score += 1
        else:
            print("Invalid choice ❌")
            break
    
    print(f"\n🎯 You got {score}/{n} correct!")
    if score == n:
        print("🔥 Perfect score! Well done!")
    elif score > n/2:
        print("👍 Good job! Keep practicing!")
    else:
        print("💡 Don’t worry, practice more and you’ll improve!")

# Call the function
calculation()
