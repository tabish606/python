lower = int(input("enter the lowest range  :"))
upper = int(input("enter the highest range :"))
n= int(input("enter the number to be divided :"))
for i in range(lower,upper+1):
    if(i%n==0):
        print(i)