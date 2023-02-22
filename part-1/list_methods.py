#extend() --- add the elements of a list (or any iterable), to the end of the current list ()
#the first list (number) join with the second list (fruits)
#add the elements of fruits to the number list:
list_num = [1, 2, 3, 4, 5, 6]
list_fruits = ["apple", "banana", "manggo", "cherry"]
list_num.extend(list_fruits)
print(list_num)

#append() method appends an element to the end of the list
#add an element to the fruits list
list_fruits.append("orange")
print(list_fruits)

#insert() method inserts the specified value at the specified position
#insert the value "barries" as the second element of the fruit list
list_num.insert(0, 0)
list_fruits.insert(1, "berries")
#print(list_num, "\n", list_fruits)
print(list_num)
print(list_fruits)

#remove() method removes the first occurrence of the element with the specified value
#remove the "apple" element of the fruit list
list_fruits.remove("apple")
print(list_fruits)

#clear() method removes all the elements from a list
#remove all elements from the number list
list_num.clear()
print(list_num)

#index() method return the position at the first occurrence of the specified value.
#what id positon of the value "orange"
print(list_fruits.index("orange"))

#count() method returns the number of elements with specified value
#return the number of times the value "banana" appears in the fruits list
print(list_fruits.count("banana"))

#sort() method sorts the list ascending by default
#sort the list number by order and name by alphabetically
num = [8, 2, 4, 7, 5, 1, 3, 0, 9 ]
num.sort()
print(num)
name1 = ["Smith", "Williams", "Brown", "Jones", "Garcia", "Miller", "Gomez"]
name1.sort()
print(name1)

#reverse() method recverses the sorting order of the elements
#reverse the order of number and name list
num.reverse()
print(num)
name1.reverse()
print(name1)

#copy() method returns a copy of the specified list
#copy the name list
name2 = name1.copy()
#print(name2)

#pop() method removes the elements the element at the specified position
#remove the first elements of the name2 list
name2.pop(0)
print(name2)