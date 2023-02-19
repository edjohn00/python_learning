#Python Numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

#Int - or integer is a whole number, positive or negative, without decimals of unlimited length
a = 1
b = 34567299767
c = -6363524

print(type(a))
print(type(b))
print(type(c))

#Float - float or "floating point number" is a number, positive or negative containing one or more decimals also float also be scientific numbers with an "e" to indicate the power of 10.

d = 1.18
e = 1.1
f = -35.59
g = 35e3
h = 123E4

print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

#Complex - number are writteb with a "j" as the imaginary part

i = 4+4j
j = 1j
k = -8j

print(type(i))
print(type(j))
print(type(k))

#Type Conversion - you can convert from one type to another with the int(), float(), and complex() methods:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#--------------------------------
num1 = 79
num2 = 1

print(num1 + num2) 

#this is how to convert an integers to string
number1 = 55 #this is a string
number2 = str(number1) #you need to type "str" short for string to convert the interger to string
print("this is now a string " + number2) 

#Function - is just a block of code which does a particulae task

#basic way to get the MAXIMUM and MINIMUM
#this is how to get the max (maximum) or the higher number
print(max(5, 3, 9, 2))

#this is how to get the min (minimum) or the lowest number
print(min(5, 3, 9, 2))

#this is how to estimate a number, we use "round"
print(round(6.4))

#this is how to convert a particular number to a binary string, use "bin"
print(bin(344)) 

#python has also a built-in module called math which extends the list of mathematical functions
from math import * 
print(sqrt(100))
