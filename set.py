#it remove the redundency
s = {1,2,3,4,5,5,5,5}
print(s)

#convert the list into set to remove duplication

l = [1,2,2,3,4,5,5,2,3,4,5,6,7,5]
s1 = set(l)
print(s1)

#we can also convert into list also

l1 = list(s1)
print(l1)

#add data

s.add(9)
print(s)

#remove(raise error) or discard(no error)

#s.remove(7)
s1.discard(8)
print(s)

# union 
s2 = {1,2,3,4}
s3 = {2,3,4,5,6}
union = s2 | s3
print(union)

#intersection

intersection = s2 & s3
print(intersection)