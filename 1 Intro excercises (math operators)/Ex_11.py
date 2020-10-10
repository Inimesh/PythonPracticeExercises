## Programme to convert from miles per US gallon to Litres per 100 km

# Take input from the user

MPG = float(input("Please enter a value in miles per gallon: "))

# converting from MPG to kmPG, as mile to km ratio is 1:1.60934
kmPG = MPG * 1.60934
# converting from kmPG to km/L, as US gallon to litre ratio is 1:3.78541
kmPL = kmPG/3.78541
# converting from kmPL to L/100km
conv = 1.00 / kmPL
LP100km = conv * 100
#Printing result
print('%.4g' % LP100km)
