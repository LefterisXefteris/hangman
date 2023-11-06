import random

word_list = ["cherry", "lady", "ocean", "germany", "travel"]
guessed_letters = set()

def ask_for_input():
    while True:
        guess = input("Guess a letter: ").lower()
        if guess.isalpha() and len(guess) == 1:
            guessed_letters.add(guess)
            check_guess(guess)
            if guess in guessed_letters:
                print(f"Letter {guess} already in set")
            if guess in word_list:
                print(f"{guess} is in the word_list")
            else:
                print(f"Letter {guess} not in the word_list")
        else:
            print("Invalid letter. Please enter a single alphabetical character.")

def check_guess(guess):
    guess = guess.lower()

    if guess in guessed_letters:
        print(f"Letter {guess} already in set")
    elif guess in word_list:
        print(f"{guess} is in the word_list")
    else:
        print(f"Letter {guess} not in the word_list")

ask_for_input()
