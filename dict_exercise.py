
user = {}
name  = input("what is your name : ")
age = input("what is your age    : ")
fav_mov = input("your fav movie seprated by comma : ").split(',')
fav_song = input("your fav song seprated by comma : ").split(',')

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_mov
user['fav_songs'] = fav_song
for key,value in user.items():
    print(f"{key} : {value}")

    
    