#Dictionaries are used to store data values in key:value pairs, 
#is a collection which is ordered*, changeable and do not allow duplicates.
#You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces ({}). A colon (:) separates each key from its associated value:
#also we can also mixed data types in dictionaries
info_dict = {
    "first_name" : "John Eddie",
    "last_name" : "Ablao",
    "age" : 22, #integer
    "nationality" : "Pilipino",
    "isAlive" : False, #boolean
    "hobbies" : ["overthink", "playing online games", "crying in night"] #list - using a square bracket

}
print(info_dict)

#to get the only value of first name use square bracket and there key-value 
print(info_dict["hobbies"])

#to get how many items (key value pairs) type len
print(len(info_dict))

#to check if what data type is 
print(type(info_dict))



