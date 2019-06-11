def reverse(n):
    return rev
rev = 0
num = int(input("enter the number for reverse"))
while num>0:
    dig =num%10
    rev =rev*10+dig
    num= num//10
print(reverse(rev))
