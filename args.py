# *args
#we can pass more than two arguements in function using (*args) statement
a=int(input("first num : "))
b=int(input("second num : "))
c=int(input("third num : "))
d=int(input("fourth num : "))
def sum(*args):
    
    total = 0
    for num in args:
        total = total+num
    return total
print(sum(a,b,c,d))
