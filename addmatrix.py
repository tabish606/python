m = int(input("enter the row of matrix :"))
n = int(input("enter the column of matrix :"))
mat1 = []
mat2 = []
for i in range (0,n):
    mat1.append([])
for i in range (0,m):
    for j in range (0,n):
        mat1[i].append(j)
        mat1[i][j] = 0
for i in range(0,m):
    for j in range(0,n):
        print("enter in row : ", i+1 , "enter in column : ", j+1," of FIRST MATRIX")
        mat1[i][j] = int(input())
print ("FIRST MATRIX",mat1)
     
for i in range(0,n):
    mat2.append([])
for i in range(0,m):
    for j in range(0,n):
        mat2[i].append(j)
        mat2[i][j]=0
for i in range (0,m):
    for j in range(0,n):
        print("enter in row : ",i+1,"enter in column : ",j+1, "of SECOND MATRIX" )
        mat2[i][j]= int(input())
print("SECOND MATRIX : ",mat2)
sum = []
for i in range(0,n):
    sum.append([])
for i in range(0,m):
    for j in range(0,n):                                     
        sum[i].append(j)                                     
        sum[i][j]=0
for i in range (0,m):
    for j in range (0,n):
        sum[i][j]= mat1[i][j]+mat2[i][j]
print(sum)        
print("Multiplication")
multi = []
for i in range(0,n):
    multi.append([])
for i in range (0,m):
    for j in range (0,n):
        multi[i].append(j)
        multi[i][j]=0
for i in range(0,m):
    for j in range(0,n):
         multi[i][j]=0
         for k in range(0,m):
            multi[i][j]= multi[i][j]+(mat1[i][k]*mat2[k][j])
print(multi)                        





