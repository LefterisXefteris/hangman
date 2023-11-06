import random

class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = set()

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print( "Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1 
        else:
            self.num_lives -= 1
            print("Sorry, {letter} is not in the word.")
            print("You have {num_lives} lives left.")



    def ask_for_input(self):
        while True:
            guess = input("Type a letter").lower()
            if guess.isalpha() and len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")

            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.add(guess)

                

word_to_guess = "example"
game = Hangman(word_to_guess)
game.ask_for_input()