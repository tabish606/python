#creat dictionary
#1
user = {'name' : 'Tabish','age' : 24 }
print(user)
#2

user1 = dict( name = 'tabish',age = 24 )
print(user1)
print(type(user))

#input data in dictionaries

user2 = {}

user2['name'] = 'tabish ansari'
user2['age']  = 24 
print(user2)

#in keywords
user_info = {
    'name' : 'jhon',
    'age ' : 23,
    'fav_movie' : ['a','b']
    
}
#for keys
if 'name' in  user_info :
    print("present")

#for values
if "jhon" in user_info.values():
    print("present")

#iterations or for loops
#it prints all keys
for i in user_info:
    print(i)

# it prints all values

for i in user_info.values():
    print(i)
    #or
#for i in user_info:
 #   print(user_info[i])    

