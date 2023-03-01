#Return keyword is to exit a function and return a value.
#in order to get a value from a function in any programming language, we use the return() statement likewise the return() statement is used to exit a function and returns a value from a function
#to let a function return a value, use the return statement
def my_function():
    return 5 + 7
print(my_function())

#another example of return using input type
def function_num(num1, num2):
    return num1 + num2

num1 = int(input("Enter first num: ")) #convert string to intgers to add two numbers
num2 = int(input("Enter second num: "))
print(function_num(num1, num2))
#always remember that only string can concatenate 
