import random

def get_level():
    while True:
        try:
            level = int(input("Enter the level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")

def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError("Invalid level. Please provide 1, 2, or 3.")
    
    return random.randint(10 ** (level - 1), 10 ** level - 1)

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        tries = 0
        while tries < 3:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == correct_answer:
                    print("Correct!")
                    score += 1
                    break
                else:
                    print("EEE - Incorrect answer. Try again.")
            except ValueError:
                print("EEE - Invalid input. Try again.")

            tries += 1

        if tries == 3:
            print(f"The correct answer was {correct_answer}.")

    print(f"Your final score is: {score} out of 10.")

if __name__ == "__main__":
    main()
