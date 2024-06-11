import random

names_string = input("Input a few names (comma separated)\n")

names = names_string.split(",")

# get list length
list_len = len(names)

# generate random number between 0 and list length, round to nearest whole number
rand_pos = round(random.randint(0, list_len - 1))

# grab item at random num position
print("Randomly grabbed name from list: " + names[rand_pos])
