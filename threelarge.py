def greater(num1,num2,num3):
    if num1>num2 and num1>num3:
        return f"{num1} is greater"
    elif num2 > num3:
        return f"{num2} is large"
    return f"{num3} is large"
a = int(input("enter first number  : "))
b = int(input("enter second number : "))
c = int(input("enter third number  : "))
print(greater(a,b,c))