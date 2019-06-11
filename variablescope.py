x=5 #global variable
def fun():
    global x
    x = 7 #local variable
    return x
print(x) #before function called
print(fun()) #function called
print(x) #after function called