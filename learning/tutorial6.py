#  WHILE LOOPS | ITERATING COLLECTION | BREAK KEYWORD

"""
    INDENTATION - is used to Indicate what statements are included inside the WHILE Loop

    WHILE LOOP - a Statement that will repeat a block of code as long as it's condition fulfilled.
    syntax: 
        while valOne > valTwo:
            #do something
"""
age = 12

# while age < 18:
#     print("Age is Still Young: " , age)
#     age = age + 1

"""
    ELSE in WHILE Loop - ELSE is added to the bottom of a while loop so that it can execute code when the loop is done
    syntax:
        while valOne > valTwo: 
            #do something
        else:
            #do something
"""
# age = 12

# while age < 18:
#     print("Age is Still Young: " , age)
#     age = age + 1
# else:
#     print("Age is Legal Age: " + str(age))

"""
    WHILE Loop in COLLECTIONS - can be used to access every item in a COLLECTION (List & Tuples) since it is indexed and ordered
"""
# studentID = [200123, 200124, 200125, 200126, 200127, 200128]

# i = 0

# while i < len(studentID):
#     print(studentID[i])
#     i = i + 1

"""
    BREAK Keyword in WHILE Loop - is used to stop the loop no matter what the condition is
"""
# while True:
#     print("Hello pips")
#     break

"""
    CONDITIONS in WHILE Loop - you can use any Conditional Statement inside a WHILE Loop
"""
numbers = [1,2,3,4,5,6,7,8,9,10]

i = 0

while i < len(numbers):
    if(numbers[i] % 2 == 0):
        print("Even Number: " + str(numbers[i]))
    else:
        print("Odd Number: " + str(numbers[i]))
    i = i + 1