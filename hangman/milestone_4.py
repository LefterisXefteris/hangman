import random

class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = set()

        print(f"The chosen word is: {self.word}")

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1 
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.") # Use 'guess' instead of 'letter'
            print(f"You have {self.num_lives} lives left.")
            if self.num_lives == 0:
                print("You lost!")
                

    def ask_for_input(self):
        while True:
            print(' '.join(self.word_guessed))  # Show the current state of the word
            guess = input("Type a letter: ").lower()
            if guess.isalpha() and len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.add(guess)

    def play_game(self):
         while self.num_lives > 0 and self.num_letters > 0:
            self.ask_for_input()
                
            if self.num_letters <= 0:
                print('Congratulations. You won the game!')
                return
            elif self.num_lives == 0:
                print( 'You lost!')
                
            

word_list = ["cherry", "lady", "ocean", "germany", "travel"]
game = Hangman(word_list)
game.play_game()