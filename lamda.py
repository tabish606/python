#normal function
def add(a,b):
    return a+b
print(add(4,3))    

#lambda expression
add2 = lambda a,b : a+b  #lambda function does not need name of function
print(add2(2,3))

multiply = lambda a,b : a*b
print(multiply(2,3))

# is even check 
#def is_even(a):
#    return a%2 == 0 #it return True if even else false
#print(is_even(8))  
#print(is_even(9))  

is_even2 = lambda a : a%2 == 0
print(is_even2(11))
print(is_even2(8))

#print last character

#def last_char(s):
#    return s[-1]
#print(last_char("tabish"))    

last_char2 = lambda s : s[-1]
print(last_char2("tabish"))