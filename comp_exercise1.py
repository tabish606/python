def rev_string(s):
    return [name[::-1] for name in s]
print(rev_string(["tabish","ansari"]))    

def data_types(l):
    return [str(i) for i in l if( type(i)==int or type(i)== float )]
print(data_types([1.0,2,2.4,'tab',True ,False]))    