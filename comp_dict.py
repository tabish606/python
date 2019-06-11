#print squares

square = {f" square of {num} is  " : num**2 for num in range(1,11)}
print(square)
for k,v in square.items():
    print(f" {k} : {v}")

# word counter

string = "tabish ansari"

word_count = { char: string.count(char) for char in string}
for k,v in word_count.items():
    print(f" {k} : {v}")

# if else
#print odd even
odd_even ={ i : ("even" if i%2 == 0 else "odd") for i in range (1,11)}
print(odd_even)
