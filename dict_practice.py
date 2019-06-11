name = input("what is your name :")
age = input("what is your age ;")
f_name = input("what is your father name : ")
m_name = input("what is your mother name : ")
user_info1 = {}
user_info1["name"] = name
user_info1["age"] = age

user_info2 = {}
user_info2["father name"] = f_name
user_info2['mother name'] = m_name

#print(user_info1)
#print(user_info2)
user_info1.update(user_info2)
print(user_info1)


#sum of all values
sum = 0
s = {1:1,2:4,3:9,4:16} 
for i in s.values():
    sum += i
print(sum)
     
    