#if statement is basically just giving python a condition, these condition can be used in several ways, most commonly in "if statements" ang loops
#Python Conditions and If statements (the usual logical conditions from mathematics)
    # Less than: < 
    # Greater than: >
    # Less than or equal to: <=
    # Greater than or equal to: >=
    # Equals: ==
    # Not Equals: !=
#If
#this conditionas can be used in several ways, most commonly in "if statements and loop" and it is written by using the if keywords
a = 10
b = 20
if a < b:
    print("yes")

c = "John"
d = "John"
if c == d:
    print("C is equal to D")

#Elif
#is python's way saying "if the previous conditons were not true, then try this condition"
e = 33
f = 33
if e > a:
    print("E is higher than A")
elif a == b:
    print("A and B are equal")

#Else
#catches anythinf which isn't caught by the preceding conditions
g = 100
h = 120
if g < h:
    print("G is lower than H")
else:
    print("G is higher than H")

i = True
j = 34
if i == True:
    print("I is true")
else:
    print("I is false")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

if num1 < num2:
    print("Num1 is less than Num2")
elif num1 > num2:
    print("Num1 is greater than Num2")
else:
    print("Num1 and Num2 is equal")




