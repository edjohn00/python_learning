#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#Lists are created using square brackets:

countries = ["USA", "Japan", "Philippines", "Korea", "Taiwan", "Canada"]
print(countries)

#always remember in python or programming in general numbers are counting from zero 
#if you want to print one by one like you want to print "Japan" all you need to do is use square brackets then insert the index number like 1
print(countries[1])

#this is how to get the index value of japan insert another square bracket then add the number
print(countries[1][0]) 

#if you want to get the index from 1 - 4 or Japan - Canada this is how works
print(countries[1:])
#if you use negative sign it will print the last value in the list
print(countries[-1])

#if you want to check the type of the particular variable insert "type" word to print function
print(type(countries))

#also you can change the particular value of the list 
countries[0] = "United Kingdom"
countries[5] = "Australia"
print(countries)

#you want to see how many index value in the variable you you need is to add "len" in the print
print(len(countries))

#also in list we can mix defferent data type in the list
mix_variables1 = [1, "USA", "Japan", 5, "Canada", True]
print(mix_variables1)
print(type(mix_variables1))


#we have a two types of printing list one is using square bracket and two is using a round bracket syntax list((""))
mix_variables2 = list(("Anna", 100, False))
print(mix_variables2)
print(type(mix_variables2))