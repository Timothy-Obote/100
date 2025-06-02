#Make 2 utility functions
def add (numb1, numb2):
    return numb1 + numb2 

def subtract(numb1, numb2):
    return numb1 - numb2

#Passing two function into another function take functions as arguments 
def function_plus_one(func, numb1, numb2):
    return func(numb1, numb2) + 1

print(function_plus_one(subtract, 5, 6))

#Returning a function from another function
def werid_function(fun, numb):
    if numb == 1:
        return fun
    return numb

print(werid_function(add, 5)(10, 20))  
