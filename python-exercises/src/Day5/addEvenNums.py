target = int(input("Enter a number between 0 and 1000"))

total = 0

if 0 < target > 1000:
    print("Invalid number entered")
else:
    for number in range(1, target + 1):
        if number % 2 == 0:
            total += number

print(f"Total of all numbers added up to entered number: {total}")
