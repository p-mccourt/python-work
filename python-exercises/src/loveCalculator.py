print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?")

combined_name = name1.lower() + name2.lower()

true_count, love_count, love_score = 0, 0, 0

true_chars = {'t', 'r', 'u', 'e'}
love_chars = {'l', 'o', 'v', 'e'}

for char in combined_name:
    if char in true_chars:
        true_count += 1
    if char in love_chars:
        love_count += 1

love_score_str = str(true_count) + str(love_count)
love_score_int = int(love_score_str)

if love_score_int < 10 or love_score_int > 90:
    print(f"Your love score is {love_score_int}, you go together like coke and mentos!")
elif 40 <= love_score_int <= 50:
    print(f"Your love score is {love_score_int}, you are alright together!")
else:
    print(f"Your love score is {love_score_int}")
