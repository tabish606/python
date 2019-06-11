#fromkeys method gives same values to each keys
#it gives individually a,b and c to unknown
user_info = dict.fromkeys("abc",'unknown')
print(user_info)

#using list
#it gives each keys to unknown(we can use tuple also)
user_info1 = dict.fromkeys(['name','age','state'],'unknown')
print(user_info1)

#get method it does not raise an error when i give the false keys it prints None

d = {'name':'unknown','age':'unknown','state':'unknown' }
#it prints name values
print(d.get('name'))
print(d.get('names'))
  
  #in keywords in get method

if d.get('name'):
      print("present")
else:
      print("not present")

# we can use subtitute of None in get method
print(d.get('hos','not found'))
#if same keys exist its overwrite the values with nextone


#clear method 
#its clear the dictionaries
#d.clear()
#print(d)

#copy method

d1 = d.copy()
print(d1)

#check equality

print(d1 is d)








