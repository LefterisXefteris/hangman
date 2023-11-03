import random

word_list = ["cherry", "lady", "ocean", "germany", "travel"]
word = random.choice(word_list)

print(word)


def is_valid_letter(letter):
    if len(letter) != 1:
        return False
    if not letter.isalpha():
        return False
    return True


letter = input("Enter a letter: ")
if is_valid_letter(letter):
    print(f"{letter} is a valid letter, Good guess!")
else:
    print(f"{letter} is not a valid letter, Oooops")