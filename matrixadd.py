def square_list(l):
     square = []
     for i in l:
          square.append(i**2)
     return square
numbers = list(range(1,5))
print(square_list(numbers))
