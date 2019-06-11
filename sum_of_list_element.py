n = int(input("enter the order of list : "))

l = [int(input()) for i in range(n)]
print(l)
sum = 0
for i in l:
    sum = sum + i
print("sum of elements = " ,sum)       