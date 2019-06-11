n = int(input("enter the number to be check :"))
for i in range(2,n):
    if n%i==0:
        print("Non prime")
        break
else:
        print("prime")