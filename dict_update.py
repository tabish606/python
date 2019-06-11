user_info = {
    'name' : 'Tabish',
    'age' : 23,
    'fav_movies' : ['Gajhini','pk']
}

more_info = {
    'state': 'UP',
    'HOBBIES' : ['coding', 'playing games']
}

user_info.update(more_info)
print(user_info)
# there is no any updation using blank dictionaries
user_info.update({})
print(user_info)