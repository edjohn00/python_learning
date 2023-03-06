#if statement is basically just giving python a condition, these condition can be used in several ways, most commonly in "if statements" ang loops
#Python Conditions and If statements (the usual logical conditions from mathematics)
    # Less than: < 
    # Greater than: >
    # Less than or equal to: <=
    # Greater than or equal to: >=
    # Equals: ==
    # Not Equals: !=
    # AND: True if both operands are True
    # OR: True if either of the operands is True
    # NOT: True if the operand is False

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

#Exercise create that tell to user weather it's passed or failed, if your score is 50 or more
score = int(input("Enter you score: "))

if score >100 or score <0:
    print("Score is invalid!!")
elif score >= 50:
    print("You have passed the exam!")
    print("Congrats")
else:
    print("You failed, Try again")

#this is how you can check wheather is string or integers

value1 = input("Input a value: ") # if you want to check string you don't need to convert it to intergers

if type(value1) == str:
    print(value1 + " is a string")
else:
    print(value1 , " is not a string")

#to check if the intergers is devided by 5
value2 = int(input("Input a value you want to convert: "))

if value2 %5 == 0:
    print(value2 , " can be divided by 5")
else:
    print(value2 , " can't divided by 5")

#check if the length of the sentence us less than 10
sentence = input("Input a sentence: ")

if sentence < 10:
    print(sentence + "this sentence is less than 10")
else:
    print(sentence + "is more than 10")






