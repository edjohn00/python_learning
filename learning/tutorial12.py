#CLASSES & OBJECT 
"""
    Onject Oriented Programming - it aims to implement real world object / entities its attributes and behavior into programming so that we can replsent it in our game, software or applications.

    Objects - anything that has an attribute and a purpose is an object.
        example:
        * Game Characters
        * Real Life People (Student, Employees)
        * Real Life Objects (Fruits, Table)

    Class - used in programming to make a blueprint for our object. It will represent their attribute and purpose
        example:
            * Game Characters
                * Purpose
                    * Physical Attack
                    * Magic Attack
                * Attributes
                    * NAME
                    * HP
                    * MP
    
    Creating Classes
        Syntax:

        class className:
            #attributes
            #purpose/functions
"""
# class HeroChar:
#     name = "Name"
#     hp = 100
#     mp = 50
#     atk = 12
#     lvl = 1

"""
    Creating Classes
        Syntax:

        class className:
            #attributes
            #purpose/functions

        Identifier = className()
"""
# class HeroChar:
#     name = "Name"
#     hp = 100
#     mp = 50
#     atk = 12
#     lvl = 1

# charOne = HeroChar()
# charTwo = HeroChar()
"""
    Creating Classes
        Syntax:

        class className:
            #attributes
            #purpose/functions

        Identifier = className()

        Identifier.attribute = value
        print(Identifier.attribute) 
"""
# class HeroChar:
#     name = "Name"
#     hp = 100
#     mp = 50
#     atk = 12
#     lvl = 1

# charOne = HeroChar()
# charTwo = HeroChar()

# charOne.name = "EdiWow"
# charOne.lvl = 15
# charTwo.name = "Hatdog"
# print(charOne.name)
# print(charOne.lvl)
# print()
# print(charTwo.name)

class Product:
    name: "Name"
    price: 1000
    isAvailable: True
    quantity: 1000
    ml: "10ml"

productOne = Product()
productTwo = Product()

productOne.name = "Milk"
productOne.price = 100
productOne.isAvailable = False
print(productOne.name)
print(productOne.isAvailable)
print()

productTwo.name = "Alcohol"
productTwo.price = 80
productTwo.isAvailable = True
productTwo.quantity = 10
productTwo.ml = "330ml"
print(productTwo.name)
print(productTwo.isAvailable)

