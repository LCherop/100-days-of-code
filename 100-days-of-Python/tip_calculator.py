print("Welcome to the tip calculator!")
bill = input("What was the total bill?\n")
perc = input("What percentage tip would you like to give? 10, 12, or 15?\n")
pple = input("How many people are to split the bill?\n")

# new_bill = (bill * .perc)+bill
#new_bill/pple

perc1 = float(perc)/100
new_bill = (float(bill)*perc1)+float(bill)
tip = new_bill/float(pple)
rounded = round(tip,2)
print(f"Each person should pay: {rounded}")