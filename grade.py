sub1 = int(input("enter the marks of first subject :"))
sub2 = int(input("enter the marks of second subject :"))
sub3 = int(input("enter the marks of third subject :"))
sub4 = int(input("enter the marks of fourth subject :"))
avg = (sub1+sub2+sub3+sub4)/4

if avg>=90:
    print("Grade A")
elif(avg>=80 and avg<90):
    print("Grade B")
elif(avg>=70 and avg<80):
      print("Grade C ")
elif(avg>=60 and avg<70):
     print("Grade D")