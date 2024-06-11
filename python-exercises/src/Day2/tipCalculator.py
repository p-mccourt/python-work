# small program to calculate how much to tip based on a bill
print("Welcome to the tip calculator!")

# get total bill amount from user
bill_amount = input("What was the total bill? $")

# convert total bill amount to float
bill_amount = float(bill_amount)

# get tip amount from user
tip_amount = input("How much tip would you life to give? 10, 12, or 15?")

# convert tip amount to float
tip_amount = float(tip_amount)/100

# get added tip value
final_bill = bill_amount + (bill_amount * tip_amount)

# get how much people split bill form user
amount_people = input("How many people split the bill?")

# get amount ot pay per person
amount_pp = round(final_bill/float(amount_people), 2)

# ensure system displays to 2 dp
amount_pp_2dp = "{:.2f}".format(amount_pp)

print(f"Each person should pay ${amount_pp_2dp}")

