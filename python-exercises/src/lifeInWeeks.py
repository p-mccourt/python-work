age = input()

# get years left until 90
time_until_90 = 90 - int(age)

# get weeks in 1 year
weeks_in_year = 52

# get weeks left in users life
weeks_left_in_life = time_until_90 * 52

# use f string to output result
print(f"You have {weeks_left_in_life} weeks left")
