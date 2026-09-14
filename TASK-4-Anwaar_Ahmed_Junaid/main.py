def main():
    score = 0

    print("======= General Knowledge Quiz =======\n")
    print("Answer the following 3 questions.\n")

    # Question 1
    answer1 = input("1. What is the capital of France? ").strip().lower()
    if answer1 == "paris":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! The correct answer is Paris.\n")

    # Question 2
    answer2 = input("2. How many continents are there in the world? ").strip().lower()
    if answer2 == "7" or answer2 == "seven":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! The correct answer is 7.\n")

    # Question 3
    answer3 = input("3. Which planet is known as the Red Planet? ").strip().lower()
    if answer3 == "mars":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! The correct answer is Mars.\n")

    # Final Score
    print("======= Quiz Completed =======")
    print(f"Your Final Score: {score}/3")

    if score == 3:
        print("Excellent! You got all answers correct!")
    elif score == 2:
        print("Good job!")
    else:
        print("Keep practicing!")


if __name__ == "__main__":
    main()