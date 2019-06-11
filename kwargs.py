#kwargs (keyword argument)
#it changes  into dictionary 
def func(**kwargs):
    
    print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k} : {v}")
        
func(f_name = "tabish", l_name = "ansari")  
#dictinary unpacking
d = {"name" : "bigde nawab", "age"  : 23}
func(**d) #if we write d without aistic(*) so it will raise error  
