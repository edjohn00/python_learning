# Function | Parameters or Arguments | Return Values
"""
    Functions - Are used to organize and divide specific tasks in a program that will only run when itis called

    Indentation - is used to Indicate what statements are included inside a Function

    Creating Function
    Syntax:                      
        def function_name():         
            #Do Something     

        Calling a Function
    Syntax:                      
        def function_name():         
            #Do Something          

        function_name()       
"""
# def sayHello():
#     print("Hello")
#     print("World")
# sayHello()

"""
    Argunments or Parameters - are values passed inside a Function that will be used to perform tasks
    Syntax:                            
        def function_name(parameters):          
            #Do Something        
        function_name(parameter)                   
"""
# name = input("Enter Name: ")

# def sayHello(name):
#     print("Hello " + name)

# sayHello(name)

# fname = input("Enter your first name: ")
# lname = input("Enter your last name: ")

# def info(fname, lname):
#     print("Hello my Name is " + fname + " " + lname)

# info(fname, lname)

"""
    Return Values - is a values retured after a function is done executing it is used to get result from a function that computes or does something that needs a result 
    Syntax:
        def function_name(parameters):
            return value
        
        function_name(parameter)
"""
def square(num):
    multiply = num * num
    return multiply

num = int(input("Input a Number: "))
result = square(num)

print(result)
