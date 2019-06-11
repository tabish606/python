#parameter order means i have four types parameter
#PADK

#parameter                                   (normal parameter like a,b etc)
#*args
#default parameter                            (pass the values of dictiinaries in parameter)        
#**kwargs    
#it is a sequence of parameters if we does not follow so error occurs definately
#example
def order_parameter(name,*args,last_name = "unknown",**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
order_parameter("tabish",1,2,3,"ansari",a=1,b=2)