n = int(input("enter the range of pattern :"))
#n=3
for i in range(1,n+1):
    for j in range (0,n-i):
        print (" ",end = "  ")
    for k in range (1,i+1):
        print(k, end = "  ")
    for l in range (1,i):
        print(i-l,end = "  ")
            
    print()
for i in range(n-1,0,-1):
    for k in range(0,n-i):
        print(" ",end = "  ")
    for j in range(0,i): 
        print(j+1, end = "  ") 
    for l in range (i-1,0,-1):
        print(l, end = "  ")
    print()    


