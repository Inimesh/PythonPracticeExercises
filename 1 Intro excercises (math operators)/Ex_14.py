## Converting from feet and inches to cenitmetres

## Taking input of number of feet and inches from user
feet = float(input("Please enter in the number of feet: "))
inches  = float(input("And now inches:"))

# Conversion factors
foot_to_inch = 12
inch_to_cm = 2.54

# Converting values
feet_in_inches = feet * foot_to_inch
inches += feet_in_inches

cm = inches * inch_to_cm

# Printing outputs
print("That is equivalent to %.2f cm" % cm)
