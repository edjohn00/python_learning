#What if you want to include a quote character as part of the string itself? Your first impulse might be to try something like this:
print("This string contains a single quote (') character.") #type of quote character within the string, the simplest way is to delimit the string with the other type. If a string is to contain a single quote, delimit it with double quotes and vice versa:

#STRING - are the sequences of character data. The string type in Python is called str.
name = 'Anna'

print('Hi.\nHow are you')
print(name)

#to get the letter in character of the variables 
print(name[0]) #we need to use squere bracket and 0 now zero represent the first letter, in Python or in programming in general numbers start counting by zero.

#to convert the character of the variables in uppercase & lowercase
print(name.upper()) #use the ".upper" and open and close round bracket to uppercase all the value
print(name.lower()) #then ".lower" and open and close round bracket to lowercase

#to check if the character is lower and upper case
print(name.islower()) #use ".islower" then it will response boolean (True or False)

#to get the amount of the character in the variable
name2 = "Alexander"

print(name2)
print(len(name2)) #type len, open bracket the variable name then close bracket

#to get the index number of the variable
print(name2.index('a')) #type the variable name the .index open round bracket and quotation mark then the letter you want to count

#to replace a text
print(name2.replace("e", "i"))