#item method
#it prints dictionaries in tuples.
user_info = {
    'name' : 'jhon',
    'age ' : 23,
    'fav_movie' : ['a','b']
    
}
user_item =  user_info.items()
print(user_item)
print()
#for loop
#any variable can use key and values

for key,value in user_info.items():
    print(f"key is {key} and value is {value} ")

print()
#add datA

user_info['fav_song'] =  ['g','h','i']    
print(user_info)
print()
#pop method

popped_item = user_info.pop('fav_song')
print(f"popped item is {popped_item} ")
print(user_info)
print()


#popitem
# itb deleted randomly any keys with values
popped_item = user_info.popitem()
print(f"popped item is {popped_item} ")
print(user_info)
print()


