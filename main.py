total_bill = input("what was the total bill ?")

tip_percentage = input("what perctentage tip would you like to give ? 10,12,15 ?")

individual_cost = input("how many people to split the bill ?")

total_bill = float(total_bill)
tip_percentage = float(tip_percentage)
individual_cost = float(individual_cost)


tip = total_bill*(tip_percentage/100)


total_cost = total_bill + tip

cost_each = round(total_cost/individual_cost, 2)



print(f"each person should pay {cost_each}")