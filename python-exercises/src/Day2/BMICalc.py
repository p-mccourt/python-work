# 1st input: enter height in metres e.g. 1.65
height = input()

# 2nd input: enter weight in kilograms e.g.: 72
weight = input()

# convert str inputs to float
height, weight = float(height), float(weight)

# calculate BMI
bmi = float((weight/(height ** 2)))

# round result to 2 d.p
bmi = round(bmi, 2)

# print to screen
print("BMI is", bmi)
