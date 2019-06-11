def odd_even_list(l):
    even_nums = []
    odd_nums = []
    for i in l:
        if i%2 == 0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    output = [odd_nums,even_nums]
    return output
nums = list(range(1,21))
print(odd_even_list(nums))