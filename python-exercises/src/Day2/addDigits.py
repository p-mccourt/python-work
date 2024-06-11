# exercise to print 2 numbers together based on user input

two_digit_number = input("Enter two numbers, e.g. 37\n")

# grab digits from input, cast to int
num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])

# add two integers together
result = num1 + num2

print("Result off adding numbers :", result)
