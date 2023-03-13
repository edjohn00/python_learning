# VARIABLES, DATATYPES AND INPUT | Arithmetic | Casting Data

''' 
    Variables - are used to store up data for later use 
    Basic Data Types:
    str or string (sentence, phrases, characters) | identifier = "Hello World"
    int or integers (positive & negative numbers) | identifier = 5, -2
    float (decimal numbers) | identifier = 23.73
    bool or boolean (true or false)

'''

firstName = "John" #string
lastName = 'Doe' #both double and single quotation mark is represent string
age = 18 #integers 
money = 25.35 #float
isAvailable = False #boolean

'''
    print() - used to display something in the console
    syntax: print(variable)
'''
print(firstName)
print(firstName + " " + lastName) #the + sign called concatenation - means add string together

'''
    input() - used to make the user input something in the console
    syntax: 
        variable = input()
        variable = input("Enter Something: ")
'''
name = input("Enter your name: ")
print(name)

'''
    Casting Variables - a technique used to convert a datatype to another datatype
    syntax:
        *convert numbers to string
        str(number)
        *convert string to numbers
        int(string)
        float(string)
'''
age = int(input("Enter your age: "))
print(name, age)

'''
    Arithmetic Operators - used to perform mathematical operators inside our programming language
    
        OPERATORS        RESULT
    +   additon          difference
    -   subtraction      sum
    *   multiplication   product
    /   division         quotient
    %   modulus          remainder
    //  floor divition   quotient(rounded off)
    **  exponent         power
'''

num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

result = num1 - num2
print(num1 + "-" + num2 + "=" + result)