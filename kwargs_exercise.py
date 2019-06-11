#normal way to 
#name = ["tabish" ,"ansari"]
#t = [i.title() for i in name]
#print(t)   

# using kwargs
def capital_letter(l, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]
names = ["tabish","ansari"]
print(capital_letter(names,reverse_str =  False))  #it print else statement     
print(capital_letter(names,reverse_str =  True)) #it print the if statement