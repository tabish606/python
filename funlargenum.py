def checknum(num1,num2):
    if num1>num2:
        return f"{num1} is large"
    return f"{num2} is large"
a = int(input("enter first number : "))
b = int(input("enter second number :"))
print(checknum(a,b))