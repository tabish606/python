nterms = int(input("enter the n terms :"))
n1= int(input("enter the first number :"))
n2 = int(input("enter the second number :"))
count=0
print(n1)
print(n2)
if count<=nterms:
    while count <nterms:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3)
        count +=1



