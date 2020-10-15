

x = 1

def xinc(x):
    if x == 5:
        xinc()

answer = xinc(x)

print("x =", x)
print("function:", answer)
