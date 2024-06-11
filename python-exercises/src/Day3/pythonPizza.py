print("Thank you for choosing Python Pizza Deliveries!")

# get user inputs
size = input("What size pizza do you want? S, M or L.\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

# initialise price of order
price = 0

# set up conditional logic for customer choices
if size == "S":
    price += 15
elif size == "M":
    price += 20
else:
    price += 25

if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if extra_cheese == "Y":
    price += 1

# display order total to customer
print(f"Your final bill is: ${price}")
