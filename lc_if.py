#print even nums
n = int(input("enter the range  : "))
even_nums = [i for i in range(1,n+1) if i%2==0]
print(even_nums)
odd_nums = [i for i in range(1,n+1) if i%2 != 0]
print(odd_nums)

#using else 
##print negative values if number is odd else multiply by 2

nums = list(range(1,20))

new_list = [i*2 if (i%2==0) else -i for i in nums]
print(new_list)