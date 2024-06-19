# Hangman Game
import random

word_list = ["aardvark", "baboon", "camel"]
word_guessed = False

# choose random word from word list
chosen_word = random.choice(word_list)

# populate a list with the chosen word
letter_list = []
for letter in chosen_word:
    letter_list.append("_")

print(f"Word is: {chosen_word}")

# print initial blank letter list for user
print(letter_list)

while not word_guessed:
    # ask user to guess a letter
    guess = input("Guess a letter\n").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            letter_list[i] = guess
    print(letter_list)

    # check win condition, if fulfilled exit the    loop
    if "_" not in letter_list:
        word_guessed = True

print("You guessed the word! Congrats!")
