### Meal cost wiith tax and tip

cost = float(input("Input meal cost: "))
VAT = 0.05
tip = 0.1

cost_VAT = cost * VAT
cost_tip = cost * tip
total = cost + cost_tip + cost_VAT

print("Tax: %.2f" %cost_VAT)
print("Tip: %.2f" %cost_tip)
print("Total: %.2f" %total)
