def to_power(n,*args):
    if args:
        return [i**3 for i in args]
    else:
        return ("args is empty")
num = [1,2,3]
print(to_power(3,*num))  #it print if statement bcoz args is exist 
print(to_power(2)) # it print else because no args arguement is passed