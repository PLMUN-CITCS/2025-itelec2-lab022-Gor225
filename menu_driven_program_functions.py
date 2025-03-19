def display_menu() -> None:
    """
    Displays the menu options to the user.
    """
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")

def greet_user() -> None:
    """
    Prints a greeting message.
    """
    print("Hello! Welcome!")

def check_even_odd(number: int) -> str:
    """
    Determines whether a given number is even or odd.
    Args:
        number (int): The number to check.
    Returns:
        str: A message indicating whether the number is even or odd.
    """
    return f"{number} is an Even number." if number % 2 == 0 else f"{number} is an Odd number."

def even_odd_checker_action() -> None:
    """
    Handles user input for checking even or odd numbers.
    """
    while True:
        try:
            num = int(input("Enter an integer: "))
            print(check_even_odd(num))
            break
        except ValueError:
            print("Error: Please enter a valid integer.")

def handle_menu_choice(choice: int) -> bool:
    """
    Executes an action based on the user's menu choice.
    Args:
        choice (int): The menu option chosen by the user.
    Returns:
        bool: True if the user chooses to exit, otherwise False.
    """
    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker_action()
    elif choice == 3:
        print("Exiting program. Goodbye!")
        return True
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
    return False

def main():
    """
    Main function to run the menu-driven program.
    """
    while True:
        display_menu()
        try:
            user_choice = int(input("Enter your choice (1-3): "))
            if handle_menu_choice(user_choice):
                break
        except ValueError:
            print("Error: Please enter a valid choice (1-3).")

if __name__ == "__main__":
    main()
