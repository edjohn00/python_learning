#List & Turple

'''
    Lists - a read and write collection of variables that may be used to sort certain data
    syntax: 
        Identifier = [value, value1, value2]
        persons = ["Jane", "John", "Jojo"]
'''

courses = ["BSIT", "BSME", "BSCS", "BSE", "BLIS"]

#   Reading WHOLE List - you can read a list by printing the whole list
#   syntax: print(list)
print(courses)

'''
    Reading Lists ITEMS - you can read a list by printing one of the Items inside it by using INDEX
    syntax: print(list[index])
        index - the number of where an item is on a collection
        + INDEX:      0       1       2
        - INDEX:     -3      -2      -1
        persons = ["Jane", "John", "Jojo"]
'''
print(courses[4]) #get the item "BLIS" using + index
print(courses[-1]) #get the item "BLIS" using - index

'''
    Reading Lists RANGE - you can read a list's range of items by specifying a range intex
    syntax: print(list[startIndex: endIndex])
            print(list[endIndex])
            print(list[startIndex])
'''
print(courses[1:4]) 

'''
    Assigning List ITEMS - You can assign a list item by using an INDEX and an Assignment Operator "="
    syntax: list[index] = value
    list[0] = "Jojo"
'''
courses[0] = "ACT"
print(courses)

'''
    List LENGTH - you can check the number of items in a list by usinf the len() function
    syntax: len(list)
'''
print(len(courses))

'''
    list COUNT - you can count how many times an item occurs in a list by using the count() function
    syntax: list.count(value)
'''
print(courses.count("BSIT"))


'''
    List ADD ITEMS by APPEND() - append() adds an items at the END OF THE LIST
    syntax: list.append(value)

    List ADD ITEMS by INSERT() - insert() adds an item at the SPECIFIED INDEX
    syntax: list.insert(index,value)
   
    List DELETING ITEMS by REMOVE() - remove() deletes an item based on ther value
    syntax: list.remove(value)

    List DELETING ITEMS by POP() - pop() deletes an item based on their index but if index is not specified it deletes the last item
    syntax: list.pop()
            list.pop(index)

    List DELETING ITEMS by DEL - del deletes an item based on their index but if index is not specified it deletes the whole list
    syntax: del list[index]
            del list

    Clearing a List - clear() deletes all the value in the list
    syntax: list.clear()
'''
courses.append("BSFM") #add item by append() or in the end of the list
courses.insert(0,"HATDOG") #add item by insert() or in the specified index
print(courses)
courses.remove("HATDOG") #delete item based on their value
print(courses)
courses.pop(0) #delete item based on index number
print(courses)
del courses[4] #same as pop, it will delete the item based in index but in the square bracket
print(courses)
#courses.clear() 
#print(courses)

'''
    Copying a List - copy() copies the whole list which can be assigned to a new list
    syntax: listOne = ["1Jane", "John", "Jojo"]
            lisTwo = listOne.copy
'''
courses.pop()
courses2ndSem = courses.copy()
print(courses2ndSem)

'''
    COMBINING List By ADDING - You can use "+" operator to combine lists.
    syntax: listOne = ["value1", "value2", "value3"]
            listTwo = ["value1", "value2", "value3"]
            listThree = listOne + listTwow

    COMBINING List BY APPEND() - append() combines list by appending the specified list to the end of the first list
    syntax: listOne = ["value1", "value2", "value3"]
            listTwo = ["value1", "value2", "value3"]
            listOne.append(listTwo)
'''
groupOne = ["Wade", "Sleepy", "Dopey"]
groupTwo = ["Doc", "Happy", "Bashful"]
groupThree = groupOne + groupTwo #by adding 

print(groupThree)

#groupOne.append(groupTwo) #by append
#print(groupOne)

'''
    REVERSE Lists Items - reverse() reverses the order of the List's Items
    syntax: list.reverse()
'''
groupOne.reverse()
print(groupOne)

'''
    SORT Lists Item - sort() Sort's list items by Alphabet or Value depending on the datatype
    syntax: list.sort() - Ascending Order
            list.sort(reverse=True) - Descending Order
'''
gradeOneStudents = ["Blake", "Lewis", "Roberto", "Ivan", "Aamon", "Claude", "Jorge", "Seth", "Happy", "Kagura"]
print(gradeOneStudents) # not sorted

gradeOneStudents.sort() # sorted by ASCENDEING
print(gradeOneStudents)

gradeOneStudents.sort(reverse=True) # sorted by DESCENDING 
print(gradeOneStudents)

'''
    NESTED List - a list inside a list also known as sublist
    syntax: identifier = ["value1", "value2", "value3", ["value1", "value2", "value3"]]
'''
#                                           fighter                                        marksman                                      mage
mobileLegendHeros = ["Balmond", "Freya", "Yen", "Alpha", "Aulus", "X-bord",["Wanwan", "Miya", "Beatrix", "Clint",["Edith","Roger"]], ["Kagura", "Valir", "Lunox", "Kadita"]]
#                       0          1       2       3        4         5    6   0        1         2         3    4   0       1       7    0        1        2         3
print(mobileLegendHeros)
#print only marksmans
print(mobileLegendHeros[6])
#print only mages
print(mobileLegendHeros[7])
#print only figthers
print(mobileLegendHeros[0:6])
#print kagura only in mages list
print(mobileLegendHeros[7][0])
#print only edith from marksmans list
print(mobileLegendHeros[6][4][0])
 
'''
    Tuples - a Read-ONLY Collection of variables that may be used to sort certain data
    syntax: identifier = (value, value, value)
            list = ("Jane", "John", "Jojo")

           - in turple you can't be assigned and can't delete one by one

    Casting TUPLES and LISTS
        Convert List to Tuple
        tuple(list)

        Convert Tuples to Lists
        list(tuple)
'''
phone = ("IPhone", "Samsung", "Realme", "Oppo")
print(phone)

phone = list(phone) #convert turple to list
print(phone)

phone.insert(0, "Cherry Mobile")
print(phone)









