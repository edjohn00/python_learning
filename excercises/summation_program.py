"""
    Create a Function that will accept N number of integers as arguments it should get the sum of all the integers passed in the function and return its sum

    Print the sum

    EXAMPLE:
        summationOf(1,2,3,4,5,6,7,8,9,10)

    OUTPUT:
        55
"""

# def summationOf(*sum):
#     addition = sum + sum
#     return addition

# sum = int(input("Enter a number "))
# result = summationOf

# print(result)

def summationOf(*numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum

print(summationOf(1,2,3))
