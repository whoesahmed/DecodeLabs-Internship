import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("======= Random Password Generator =======\n")

    while True:
        user_input = input("Enter password length (or type 'quit' to exit): ").strip().lower()

        if user_input == "quit":
            print("Goodbye!")
            break

        try:
            length = int(user_input)

            if length < 4:
                print("Password length must be at least 4 characters, Please try again.\n")
                continue

            password = generate_password(length)
            print(f"\nGenerated Password: {password}\n")

        except ValueError:
            print("Invalid input. Please enter a number or type 'quit'.\n")


if __name__ == "__main__":
    main()