import random

# A list to store the user's tasks
tasks = []

# Welcome message
print("=================================")
print("WELCOME TO MY PERSONAL MINI-TOOLKIT")
print("=================================")

# Main menu loop
while True:
    print("\nMAIN MENU")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Guessing Game")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    # Tool 1: Simple Calculator
    if choice == "1":
        print("\n--- SIMPLE CALCULATOR ---")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        operation = input("Choose an operation (1-4): ")

        if operation == "1":
            result = num1 + num2
            print(f"The answer is: {result}")

        elif operation == "2":
            result = num1 - num2
            print(f"The answer is: {result}")

        elif operation == "3":
            result = num1 * num2
            print(f"The answer is: {result}")

        elif operation == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"The answer is: {result}")
            else:
                print("Sorry, you cannot divide by zero.")

        else:
            print("Invalid operation.")

        # Tool 2: To-Do List
    elif choice == "2":
        while True:
            print("\n--- TO-DO LIST ---")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Back to Main Menu")

            todo_choice = input("Choose an option (1-4): ")

            if todo_choice == "1":
                task = input("Enter your task: ")
                tasks.append(task)
                print(f"Task added: {task}")

            elif todo_choice == "2":
                if len(tasks) == 0:
                    print("Your to-do list is empty.")
                else:
                    print("\nYOUR TASKS:")
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

            elif todo_choice == "3":
                if len(tasks) == 0:
                    print("There are no tasks to remove.")
                else:
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

                    task_number = int(input("Enter the task number to remove: "))

                    if task_number >= 1 and task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Removed task: {removed_task}")
                    else:
                        print("Invalid task number.")

            elif todo_choice == "4":
                break

            else:
                print("Invalid choice. Please try again.")

# Tool 3: Number Guessing Game
    elif choice == "3":
        secret_number = random.randint(1, 10)
        guess = 0

        print("\n--- NUMBER GUESSING GAME ---")
        print("I am thinking of a number between 1 and 10.")

        while guess != secret_number:
            guess = int(input("Enter your guess: "))

            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print(f"Congratulations! You guessed {secret_number} correctly!")

    elif choice == "4":
        print("\nThank you for using my toolkit. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 4.")