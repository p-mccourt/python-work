# Hangman Game
import random

word_list = ["aardvark", "baboon", "camel"]

# choose random word from word list
chosen_word = random.choice(word_list)

print(f"Word is: {chosen_word}")

# ask user to guess a letter
guess = input("Guess a letter\n").lower()


# populate a blank display list with chosen word spaces
def create_blank_spaces(word):
    blank_list = []
    for letter in word:
        blank_list.append("_")
    return blank_list


display = create_blank_spaces(chosen_word)


# function to check if users guess letter is in the chosen word
def contains_guess_letter(word, letter_guess, letter_list):
    list_pos = 0
    for letter in word:
        if letter_guess == letter:
            letter_list
            list_pos += 1
    print(letter_list)


contains_guess_letter(chosen_word, guess, display)
