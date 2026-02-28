import random
import string

def generate_password():
    print("\n--- RANDOM PASSWORD GENERATOR ---")
    try:
        length = int(input("Enter password length (min 8): "))
        if length < 8:
            print("For better security, please choose at least 8 characters.")
            return

        print("Options: 1=Letters, 2=Numbers, 3=Symbols, 4=Letters+ Numbers, 5=Mixed")
        choice = input("Enter choice (1-5): ")

        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation

        if choice == "1": PW = letters
        elif choice == "2": PW = digits
        elif choice == "3": PW = symbols
        elif choice == "4": PW = letters + digits
        elif choice == "5": PW = letters + digits + symbols
        else: print("Invalid choice."); return

        
        password = ""
        for i in range(length):
            password += random.choice(PW)

        print("\nGenerated Password:", password)

    except ValueError:
        print("Please enter a valid number.")

while True:
    generate_password()
    if input("\nGenerate another? (y/n): ").lower() != 'y':
        print("----Closing Password generator----")
        break
