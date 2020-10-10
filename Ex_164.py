## A program thta reads values from the user until a blank line is entered, and
# displays the total of all the values entered by the user (0.0 if first value
# is a blank line). USE RECURSION and no loops. ##

def adder():
    # Taking input as a string
    n = input("Please enter a number (blank to sum): ")

    # When a number is entered as a string it will be interpreted as a float and
    # the function will be called again to add another number to this value
    # This is the RECURSION CALL
    if n != "":
        n = float(n)
        return n + adder()
    # When a blank line is enterd then the function will return a zero and not
    # call the function again, effectively adding 0 to our current run of
    # additions and not call for the function to add anythin else. This is our
    # escape statement.
    else:
        return 0.0

print(adder())

### So this was my first recursion challenge and I didn't really know how to
# think about it (recursion is famously hard to get your head around). Essentially
# you set up an 'active section of code', that will carry out the operation you
# want your function to apply, followed by a return command INCLUDING the
# function call (recursive call).
#
# This sets up a chain of operations that will not terminate until a
# 'get out clause' is executed. You can think about it as visualising the
# function call with the code of the function contained in it.
#
# e.g. return n + adder()   can be seen as...
#      return n + n + adder()     which can in turn be seen as
#      return n + n + n + adder()     This goes on and on
#
# Literally 'adder()' == 'return n + adder'
#
# NOTICE that 'n + adder' is the last thing on the chains above. That means that
# all we need to do is give another return command that will terminate this chain
#
# e.g. return n + 0.0
#
# This will make the chain look like...
# return n + n + n + 0.0
#
# with each n being specified on each function call e.g.
# return 1.0 + 2.0 + 3.0 + 0.0
#
# this will simply return 6.0 and so job done! ###
