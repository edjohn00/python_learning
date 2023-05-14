#COLLECTION OF OBJECT

"""
    Creating an Object with User Input
    Syntax:                                                 Example:

        class className:                                        class Person:
            def __init__(self,a1,a2):                               def __init__(self, name):
                #initialize code                                        self.name = name

        a1 = input()                                            name = input("Enter Name: ")
        a2 = input()                                            pOne = Person(name)
        Identifier = className(a1, a2 )
"""
# class Person:
#     def __init__(self, name):
#         self.name = name
#         print(self.name + " created!")

# name = input("Enter a Name: ")
# personOne = Person(name)

"""
    Store Objects in Collection 
    Syntax:                                                 Example:

        class className:                                        class Person:
            def __init__(self, attribute)                           def __init__(self,name):
                #initialize code                                        self.name = name

        x1 = className(attribute)                               pOne = Person("David")
        x2 = className(attribute)                               pOne = Person("Jane")
        x3 = className(attribute)                               pOne = Person("Jaymar")

        listOfX = [x1,x2.x3]                                    listOfPeople = [pOne, pTwo, pThree]
"""
# class Person:
#     def __init__(self, name):
#         self.name = name

# personOne = Person("David")
# personTwo = Person("Jane")
# personThree = Person("Jaymar")

# listOfPeople = [personOne, personTwo, personThree]
"""
    Read Objects in Collection
    Syntax:                                                 Example:

        class className:                                        class Person:
            def __init__(self, attribute)                           def __init__(self,name):
                #initialize code                                        self.name = name

        x1 = className(attribute)                               pOne = Person("David")
        x2 = className(attribute)                               pOne = Person("Jane")
        x3 = className(attribute)                               pOne = Person("Jaymar")

        listOfX = [x1,x2.x3]                                    listOfPeople = [pOne, pTwo, pThree]

        print(listOfX[index].attribute)                         print(listOfPeople[0].name)
"""
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def introduce(self):
#         print("I'm " + self.name)

# personOne = Person("David")
# personTwo = Person("Jane")
# personThree = Person("Jaymar")

# listOfPeople = [personOne, personTwo, personThree]

# listOfPeople[1].introduce()

"""
    Using Loop To Read Collections
    Example:

        class Person:                                       for person in listOfPeople:
            def__init__(self, name):                            print(person.name)
                self.name = name

        pOne = Person("David")
        pOne = Person("Jane")
        pOne = Person("Jaymar")

        listOfPeople = [p1, p2, p3]
"""
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def introduce(self):
#         print("I'm " + self.name)

# personOne = Person("David")
# personTwo = Person("Jane")
# personThree = Person("Jaymar")

# listOfPeople = [personOne, personTwo, personThree]

# for person in listOfPeople:
#     print(person.name)

"""
    Using Loop To Write in Collection
    Example:

        class Person:                                       for i in range(5):
            def__init__(self, name):                            name = input("Name: ")
                self.name = name                                p = Person(name)
                                                                listOfPeople.append(p)
        listOfPeople = []
"""

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hi I'm " + self.name)

listOfPerson = []

for i in range(3):
    name = input("Enter a Name: ")
    personName = Person(name)
    listOfPerson.append(personName)

for person in listOfPerson:
    person.introduce()