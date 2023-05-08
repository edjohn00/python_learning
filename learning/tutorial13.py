#CONSTRUCTORS 

"""
    Constructors - are used to initialize an Object or simply put values on its attributes when it is created.

    __init__Function - init (initialize) function is created it is used as as a constructor.
        SYNTAX:                                         EXAMPLE:
            class objectName:                               class Character:
                def__init__(self):                              def__init__(self):
                    #initialize code                                print("Character Created")

                                                        charOne = Character()
"""
# class Character:
#     def __init__(self):
#         print("Character Created")

# charOne = Character()

"""
    Self Parameter - the self parameter in the parameter of __init__ is pertaining to itself the object that is being created.

    PS: You can change the name of the parameter as long as it is the first parameter it will always pertain to itself

    Object with Constructor
        EXAMPLE:
            class Character:
                def __init__(self, name, hp, mp, atk, lvl)
                    self.name = name
                    self.hp = hp
                    self.mp = atk
                    self.lvl = lvl
                    print(name + " Created")
            
            charOne = Character("Alenere", 100, 50, 12, 1)
"""
class Character:
    def __init__(self, name, hp, mp, atk, level):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.level = level
        print("Character Name " + self.name)
        print("Attack Speed " , self.hp)
        print("Level " , self.level)

charOne = Character("David", 200, 100, 15, 2)
charTwo = Character("John", 150, 100, 25, 5)