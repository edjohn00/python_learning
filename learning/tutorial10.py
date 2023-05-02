# Arguments
"""
    Arguments or Parameters  - are values inside a Function that will be used to perform tasks.

    def function_name(parameter/s)
        #do something

    function_name(value/s)
"""
# def message(name):
#     print("kaya pa ba " + name + "?")

# message(input("sino pagod na? "))

"""
    Arbitrary Arguments (*args) - are used if you don't exactly know how many arguments in needed in your function.

    PS. Arbitrary Arguments that is passed in will be considered as a tuple allowing it to be iterated using a loop.

    Syntax: 
    def function_name(parameters)
        #do something

    function_name(v1, v2, v3)
"""
# def sayHello(*names):
#         for name in names:
#             print("Hello " + name)

# sayHello("Anna", "John", "Doey", "Luke", "David", "Jennie")

"""
    Keyword Arguments (kwargs) - is an alternative way for sending arguments inside a function by sending arguments inside a function by specifiying the parameter name in no certain order

    Often used in combination with Arbitrary Arguments or if you don't know the order of the arguments in the function. 

    Syntax: 
    def function_name(para1, para2)
        #do something

    function_name(v1, v2, para1 = para2)
"""
# def sameLastName(*firstNames, lastName):
#     for names in firstNames:
#         print(names + " " + lastName)
# sameLastName("John", "Jannie", "Bob", "Doey", "Lisa", lastName="Hakdog")

"""
    Arbitrary Keyword Arguments (**kwargs) - used when you are uncertain on what parameter name you want to pass
    
    Syntax: 
    def function_name(**parameter):
        #do something

    function_name(kward = v1, kword = v2)
"""
# def studentInfo(**student):
#     print(student["name"])
#     print(student["course"])
#     print(student["studentNum"])
#     print(student["age"])

# studentInfo(name="John Doey", course="BSIT", studentNum=00, age=21)