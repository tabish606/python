n = int(input("enter the level of pyramid :"))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i+1) :
        print(f"{k}",end=" ")
    for l in range(1,i):
        print(f"{i-l}",end=" ")

    print("\r")
for i in range(0,n-1):
    for k in range(0,i+1):
        print(" ",end=" ")
    for j in range(1,n-i):
        print(f"{j}",end=" ")
    for l in range(1,i+2):
            print(f"{(n-1)-l}",end=" ")

    print("\r")
