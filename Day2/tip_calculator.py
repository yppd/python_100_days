print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?")) / 100
people = int(input("How many people to split the bill?"))
bill_with_tip = bill * (tip + 1)
amount_to_pay = round(bill_with_tip / people, 2)
print(f"Each person should pay: ${amount_to_pay}")
