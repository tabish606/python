n  = int(input('enter the order of list : '))

l = [int(input()) for i in range(0,n)]
l.sort()
print("largest number is : ",l[n-1])
print("2nd largest number is : ", l[n-2])

#odd even serparate list


odd_list = [i for i in l if i%2!= 0 ]
print("odd numbers list : ", odd_list)
even_list = [i for i in l if i%2==0]
print("even number list is ; ",even_list)

#merge list
n2 = int(input("enter the order of 2nd list : "))
l2  = [int(input()) for i in (0,n2)]
l3 = l2+l
l3.sort()
print(l3)