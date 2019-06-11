n = input("enter the range of pattern :")
#n=TABI
for i in range(1,len(n)+1):
    for j in range (0,len(n)-i):
        print (" ",end = "  ")
    for k in range (0,i):
        print(n[k], end = "  ")
    for l in range (i-1,0,-1):
        print(n[l-1],end = "  ")    
            
    print()
for i in range(len(n)-1,0,-1):
    for k in range(0,len(n)-i):
        print(" ", end = "  ")
    for j in range(0,i): 
        print(n[j], end = "  ") 
    for l in range (i-2,-1,-1):
        print(n[l], end = "  ")    
   
    print()    