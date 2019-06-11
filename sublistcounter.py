def sublist(l):
    count = 0
    for i in l:
        if type(i) == list:
            count +=1
    return count
lists = [1, [1,2], [3,4,5],[3]]
print(sublist(lists))
