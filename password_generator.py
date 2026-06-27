import random
import string

def generate_password(length):
    all_chars = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        string.punctuation
    )

    password = ""

    for i in range(length):
        password += random.choice(all_chars)

    return password

while True:
    print("\n===== PASSWORD GENERATOR =====")
    print("1. Generate Password")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        length = int(input("Enter password length: "))
        print("Generated Password:", generate_password(length))

    elif choice == "2":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")