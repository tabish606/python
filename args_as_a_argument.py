#it is a normal args example
def multiply(*args):
    multi = 1
    for i in args:
        multi *= i
    return multi
print(multiply(2,3,4,5,6))   

# if we want to pass the list in in args
def multiply1(*args):
    multi = 1
    for i in args:
        multi *= i
    return multi
num = [1,2,3,5]    
print(multiply1(num)) #it print complete list beacause list is packed, if we want to print multiplication of list elements so we have to unpack
print(multiply1(*num))# * operator unpacked the list and multiply each element of list


