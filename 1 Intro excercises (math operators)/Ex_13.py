## Cash register program that determines the amount of change to be given to a
## customer in candian coins

# input in cents
cents = int(input("Amount charged to customer in cents:"))

# number of toonies
toonie = cents//200
remain = cents - (toonie*200)

loonie = remain//100
remain -= loonie * 100

quarter = remain//25
remain -= quarter * 25

dime = remain//10
remain -= dime * 10

nickel = remain//5
remain -= nickel * 5

penny = remain//1

print("Toonies: %s \n" % toonie)
print("Loonies: %s \n" % loonie)
print("Quarters: %s \n" % quarter)
print("Dimes: %s \n" % dime)
print("Nickels: %s \n" % nickel)
print("Pennies: %s \n" % penny)
