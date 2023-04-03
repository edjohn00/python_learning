# Dictionary | List of Dictionaries

'''
    Dictionary - a collection of Key Pairs that is Unordered Changeable and Indexed
    syntax: identifier = {
                          keyOne : value1
                          keyTwo : value2
                          keyThree : value3
                          }
'''
studentOne = {
    "name" : "Seth",
    "course" : "BSIT",
    "studentId" : 309492,
    "age" : 19,
    "isEnroll" : True
}

studentTwo = {
    "name" : "Anna",
    "course" : "BSIT",
    "studentId" : 323333,
    "age" : 19,
    "isEnroll" : False
}

"""
    You can read a dictonary by printing the whole dictionary
    syntax: print(dictionary)
"""
print(studentOne)

"""
    Reading Dictionary ITEAMS - by specifying the Key Value
    syntax: print(dictionary[key])

    Reading Dictionary ITEAMS GET - can also use GET to read a dictionary by specifying the Key Value
    syntax: print(dictionary.get(key))
"""
print(studentOne["name"]) #>>> Seth
print(studentOne.get("name")) #using get >>> Seth

"""
    Assigning Dictionary ITEAMS - you can change a value of certain item in a dictionary by specifying the Key Value and using the Assignment Operator "="
    syntax: dictionary[key] = value

    Dictionary LENGTH - you can check the number of items (key pairs) in a Dictionary by using the len() function
    syntax: len(dictionary)

    Dictionary ADD ITEMS - you can add items on a dictionary just by assigning a non-existent key value in the dictionary
    syntax: dictionary[key] = value

    Dictionary DELETING ITEMS by POP() - deletes an item based on their key value
    syntax: ditonary.pop(key)

    Dictionary DELETING ITEMS by POPITEM() - deletes the last inserted item on the dictionary 
    syntax: dictionary.popitem()
    ps. Before python 3.7 it removes a ramdom item

    Clearing a Dictionary CLEAR() - deletes all the items in a dictionary
    syntax: dictionary.clear()

    Copying a Dictionary COPY() - copies the whole dictionary which can be assignec to a new dictionary
    syntax: student = {"name" : "ANNA", "gender" : "male"}
            studentTwo = student.copy
"""
#assigning dict
studentOne["name"] = "hakdog"
print(studentOne)

#dict length
print(len(studentOne))

#dict add item
studentOne["gender"] = "male"
print(studentOne)

#dict delete by pop()
studentOne.pop("name") #remove "name"
print(studentOne)

#dict delete by popitem()
studentOne.popitem() #remove "gender"
studentOne.popitem() #remove "isEnroll"
print(studentOne)

#dict clear
#studentOne.clear()
#print(studentOne)

#dict copy
studentThree = studentTwo.copy()
studentThree["name"] = "Jane"
studentTwo["isEnroll"] = True

print(studentTwo)
print(studentThree)

"""
    Getting ALL Keys in Dictionary KEY() - returns a list contains all the keys inside your dictionary
    syntax: dictionary.key()

    Getting ALL Values in Dictionary VALUES() - returns a list that contains all the values inside your dictionary
    syntax: dictionary.values()
"""
#Get all key in dict
print(studentThree.keys()) #dict keys

#Get all values in dict
print(studentThree.values()) #dict values

"""
    List of Dictionaries - Dictionaries inside a list
"""
students = [studentOne, studentTwo]
print(students)





