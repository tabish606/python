#print identity matrix for example
#  1  0  0
#  0  1  0
#  0  0  1
m = int(input('enter the order of matrix : '))
#list comprehension
#mat = [[] for i in range (0,m)]
#mat = [[0 for j in range(0,m) for i in range(0,m)]]
#mat = [[int(input()) for i in range(0,m)] for i in range(0,m)]
mat = []
for i in range(0,m):
        mat.append([])
for i in range (0,m):
        for j in range(0,m):
                mat[i].append(j)
                mat[i][j] = 0        
for i in range(0,m):
    for j in range(0,m):
        if (i == j):
                mat[i][j] = 1
        print(mat[i][j] ,end = "   ")
    print("\n")        
 
 