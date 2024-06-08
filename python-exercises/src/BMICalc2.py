height = float(input("Enter your height (m)\n"))

weight = int(input("Enter your weight (kg)\n"))

bmi = round(float((weight/(height ** 2))), 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif 18.5 <= bmi < 25:
    print(f"Your BMI is {bmi}, you are a normal weight")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi}, you are slightly obese")
else:
    print(f"Your BMI is {bmi}, you are slightly clinically obese")
