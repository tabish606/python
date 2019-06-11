#list comprehension

#simple list  example
#creat a list of squares

squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)    

#using list comprehension

squares1 = []

squares1 =  [i**2 for i in range(1,11)]
print(squares1)

#NOTE : in list comprehension method the  data is to be append in list is remeber and put in tha list with the loop conditons like above examples

#example2 print negative numbers

negative = [-i for i in range(1,11)]
print(negative)

#example 3 print first charcter of element

names = ['tabish', 'ansari','bigde', 'nawab']
 
first_char = [name[0] for name in names]
print(first_char) 
