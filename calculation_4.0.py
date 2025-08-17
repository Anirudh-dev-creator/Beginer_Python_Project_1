from random import randint, choice
import time

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
    start = time.time()   # start timer
    user_input = int(input(f"Enter the answer\n {a} + {b} : "))
    end = time.time()     # end timer
    taken = round(end - start, 2)  # time taken in seconds

    if result == user_input:
        print(f"✅ Correct! (Time taken: {taken} seconds)")
        return True, taken
    else:
        print(f"❌ Wrong! Correct answer: {result} (Time taken: {taken} seconds)")
        return False, taken

def subtraction():
    a = randint(10,100)
    b = randint(10,100)
    result = a - b
    start = time.time()
    user_input = int(input(f"Enter the answer\n {a} - {b} : "))
    end = time.time()
    taken = round(end - start, 2)

    if result == user_input:
        print(f"✅ Correct! (Time taken: {taken} seconds)")
        return True, taken
    else:
        print(f"❌ Wrong! Correct answer: {result} (Time taken: {taken} seconds)")
        return False, taken

def multiplication():
    a = randint(10,100)
    b = randint(10,100)
    result = a * b
    start = time.time()
    user_input = int(input(f"Enter the answer\n {a} * {b} : "))
    end = time.time()
    taken = round(end - start, 2)

    if result == user_input:
        print(f"✅ Correct! (Time taken: {taken} seconds)")
        return True, taken
    else:
        print(f"❌ Wrong! Correct answer: {result} (Time taken: {taken} seconds)")
        return False, taken

# ---- Main Program ----
user_choice = input(f"Enter the calculation method {list(operation.keys())}: ")
n = int(input("How many questions do you want to practice? : "))

def calculation():
    score = 0
    total_time = 0
    for i in range(n):
        # If random mode, pick one operator at random
        current_choice = user_choice
        if user_choice == "random":
            current_choice = choice(["+", "-", "*"])

        if current_choice == "+":
            correct, taken = addition()
        elif current_choice == "-":
            correct, taken = subtraction()
        elif current_choice == "*":
            correct, taken = multiplication()
        else:
            print("Invalid choice ❌")
            break

        if correct:
            score += 1
        total_time += taken
    
    avg_time = round(total_time / n, 2)
    print(f"\n🎯 You got {score}/{n} correct!")
    print(f"⏱️ Total time: {round(total_time,2)} seconds")
    print(f"⚡ Average time per question: {avg_time} seconds")

# Call the function
calculation()