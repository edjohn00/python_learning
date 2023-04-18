#FOR LOOP | ITERATING COLLECTIONS
"""
    INDENTATION - is used to indicate what statements are included inside the FOR Loop

    FOR Loop - a statement that is commonly used to iterate through a collection or to execute a block of code in a certain amount of times

    FOR Loop in COLLECTIONS
    FOR Loop - can be used to access every item in a COLLECTION (List & Tuples) in a very easy way
    syntax:                                         example: 
        for x in collection:                            fruits = ["Banana", "Apple", "Orange"]
            #do something                               for fruits in fruits:
                                                            print(fruit)
"""
# students = ["John", "Anna", "Jane","Fate", "Alex"]

# for name in students:
#     print(name)

"""
    ELSE in FOR Loop - is added to the bottom of a for loop so that it can execute code when the loop is done
    syntax:                                         example:
        for x in collection:                            fruits = ["Banana", "Apple", "Orange"]
            #do something                               for fruits in fruits:
        else:                                               print(fruit)
            #do something                               else:
                                                            print("No More Fruits)
"""
# students = ["John", "Anna", "Jane","Fate", "Alex"]

# for name in students:
#     print(name)
# else:
#     print("No More")

"""
    BREAK Keyword in FOR Loop - used to stop the loop earlier than its supposed to finsih
"""
# students = ["John", "Anna", "Jane","Fate", "Alex"]

# for name in students:
#     print(name)
#     break

"""
    CONDITIONS in FOR Loop - you can use any Conditional Statement inside a FOR Loop
"""
# students = ["John", "Anna", "Jane","Fate", "Alex"]

# for name in students:
#     print(name)
#     if name == "Jane":
#         print
#         break

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for number in numbers:
#     if number % 2 == 0:
#         print("Even Number: " + str(number))
#     else: 
#         print("Odd Number: " + str(number))
    
"""
    RANGE() in FOR Loop - a set of code in a soecified number of times
    syntax:                                          example:
        for x in range(y):                              for x in range(5):
            #do something                                   print(x)
"""
for x in range (3):
    print("kaya mo yan")