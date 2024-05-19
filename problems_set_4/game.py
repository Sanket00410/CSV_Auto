import random

def get_level():
    while True:
        try:
            level = int(input("Enter a positive integer for the level: "))
            if level > 0:
                return level
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def play_game(level):
    target_number = random.randint(1, level)

    while True:
        try:
            guess = int(input(f"Guess the number (between 1 and {level}): "))
            
            if guess < 1:
                print("Please enter a positive integer.")
            elif guess < target_number:
                print("Too small! Try again.")
            elif guess > target_number:
                print("Too large! Try again.")
            else:
                print("Just right! You guessed the correct number.")
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    level = get_level()
    play_game(level)

if __name__ == "__main__":
    main()
