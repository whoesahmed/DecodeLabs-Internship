def main():
    total = 0.0
    print("======= Expense Tracker =======")
    print("Enter your expenses one by one.")
    print("Type 'done' when you are finished.\n")

    while True:
        user_input = input("Enter Expense Amount: ").strip().lower()

        if user_input == "done":
            break

        try:
            amount = float(user_input)

            if amount < 0:
                print("Expense cannot be negative. Please try again.")
                continue

            total += amount
            print(f"Added: {amount:.2f} | Current Total: {total:.2f}")

        except ValueError:
            print("Invalid input. Please enter a number or type 'done'.")

    print("\n======= Summary =======")
    print(f"Total Spent: {total:.2f}")
    

if __name__ == "__main__":
    main()