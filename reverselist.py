def reverse_list(l):
    reverse = []
    for i in l[::-1]:
        reverse.append(i)
    return reverse

numbers = list(range(1,11))
print(reverse_list(numbers))

