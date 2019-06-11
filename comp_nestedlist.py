#example = [ [1,2,3], [1,2,3], [1,2,3] ]

#simple method
new_list = []
for j in range(0,3):
    new_list.append([1,2,3])
print(new_list)    

#using LC

new_list2 = [[i for i in range(1,4)] for j in range (1,4)]
print(new_list2)