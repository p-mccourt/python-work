import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []


rand_letters = []
rand_nums = []
rand_symbols = []

print("Welcome to the PyPassword Generator!")

letter_count = int(input("How many letters would you like in your password?\n"))
number_count = int(input("How many numbers would you like in your password?\n"))
symbol_count = int(input("How many symbols would you like in your password?\n"))


# get random letters for password
# loop from 0 to users desired letter count
for n in range(0, letter_count):
    # generate random index number
    rand_letter_index = round(random.randint(0, len(letters) - 1))
    # grab random letter from letters list at a random index, append to random letters list
    rand_letters.append(letters[rand_letter_index])

# rinse and repeat for numbers and symbols
for n in range(0, number_count):
    rand_number_index = round(random.randint(0, len(numbers) - 1))
    rand_nums.append(numbers[rand_number_index])

for n in range(0, symbol_count):
    rand_symbol_index = round(random.randint(0, len(symbols) - 1))
    rand_symbols.append(symbols[rand_symbol_index])

print(f"Random Letters: {rand_letters}")
print(f"Random Numbers: {rand_nums}")
print(f"Random Symbols: {rand_symbols}")
print("Generating password.....")

# generate password then shuffle it for random output
password = rand_letters + rand_nums + rand_symbols
random.shuffle(password)

# use .join to concatenating its elements into a string with no separator (empty string)
print(f"Generated password: {''.join(password)}")
