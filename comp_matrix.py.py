m = int(input("enter the row of matrix : "))
n = int(input("enter the column of matrix"))
#mat1 = [int(input()) for i in range(0,m)  ]
#print(mat1)
    

mat2 = [[] for i in range (0,n)]
mat2 = [  [0 for j in range (0,n)]  for i in range (0,m)  ]
mat2 = [[int(input()) for j in range(0,n)] for i in range (0,m) ]
print(mat2)

