def display_menu():
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    return choice

def greet_user():
    print("Hello! Welcome!")

def check_even_odd():
    try:
        num = int(input("Enter an integer: "))
        if num % 2 == 0:
            print(f"{num} is an Even number.")
        else:
            print(f"{num} is an Odd number.")
    except ValueError:
        print("Please enter a valid integer.")

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            greet_user()
        elif choice == '2':
            check_even_odd()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if _name_ == "_main_":
    main()