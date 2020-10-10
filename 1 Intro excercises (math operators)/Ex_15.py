# Programme that converts feet to inches, yards and miles,

FEET_TO_INCHES = 12
FEET_TO_YARDS = 1/3
FEET_TO_MILES = 0.000189394

feet = float(input("Enter measurement in feet: "))

print("Equal to", feet * FEET_TO_INCHES, "inches")
print("Equal to", feet * FEET_TO_YARDS, "yards")
print("Equal to", feet * FEET_TO_MILES, "miles")
