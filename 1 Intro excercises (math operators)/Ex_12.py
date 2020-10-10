## Program that finds the distance beteween two point on earth from an imput
## of start and finish latitude and longditude values

# Asking user for latitude and longditude values and converting degrees into
# radians

from math import *

t1 = radians(float(input("please enter start latitude:")))
g1 = radians(float(input("please enter start longditude:")))
t2 = radians(float(input("please enter finish latitude:")))
g2 = radians(float(input("please enter finish longditude:")))

# Using formula to convert

distance = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1-g2))
print("distance is %.2f km" % distance)
