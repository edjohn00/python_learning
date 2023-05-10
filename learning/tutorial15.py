#INHERITANCE

"""
    Inheritance 
        - allows a child class to Inherit Methods and Attributes from a parent class
        - are used to create variations of an objects

    Parent Calss - is the class where we inherit all the Functions and Attributes they are also called the Base Class or the Super Class

    Child Class - are cariation of the Parent Class they have the same functions and attributes but the Child Class has the ability to have their own functions and attributes that the Parent Class doesn't have

    Using Inheritance
        Parent Class                                    Child Class 

        class parentClassName:                          class childClassName(parentClassName):
            def __init__(self):                             pass
                #initialize code

            def objFunc(self):
                #initialize code
"""
# #PARENT CLASS
# class Person:
#     def __init__(self, firstName, lastName):
#         self.firstName = firstName
#         self.lastName = lastName

#     def introduce(self):
#         print("I am " + self.firstName + " " + self.lastName)


# #CHILD CLASS
# class Student(Person):
#     pass

# #from parent class
# personOne = Person("John", "Ablao")
# personOne.introduce()

# #from child class
# personTwo = Student("Lady", "Adda")
# personTwo.introduce()

"""
    Overriding Constructor
        Parent Class                                    Child Class 

        class parentClassName:                          class childClassName(parentClassName):
            def __init__(self):                             def __init__(self):
                #initialize code                                #initialize code

            def objFunc(self):
                #initialize code
"""
# #PARENT CLASS
# class Person:
#     def __init__(self, firstName, lastName):
#         self.firstName = firstName
#         self.lastName = lastName

#     def introduce(self):
#         print("I am " + self.firstName + " " + self.lastName)


# #CHILD CLASS
# class Student(Person):
#     def __init__(self, firstName, lastName, course):
#         super().__init__(firstName, lastName)
#         self.course = course

#     def introduce(self):
#         print("Hi I'm Name is " + self.firstName + " " + self.lastName + " and my course that I take is " + self.course)

# person = Person("Lady", "Ada")
# student = Student("Anna", "Bear", "BSIT")

# person.introduce()
# student.introduce()

"""
    Adding Attributes
        Parent Class                                    Child Class 

        class parentClassName:                          class childClassName(parentClassName):
            def __init__(self):                             def __init__(self, attributes):
                #initialize code                                super().__init__(attributes)
                                                                #additional attributes
            def objFunc(self):
                #initialize code
"""


"""
    Overriding Function
        Parent Class                                    Child Class 

        class parentClassName:                          class childClassName(parentClassName):
            def __init__(self):                             def __init__(self):
                #initialize code                                #initialize code
                                                            
            def objFunc(self):                              def objFunc (self):
                #initialize code                                #initialize code
"""


"""
    Customizing Overrode Functions
        Parent Class                                    Child Class 

        class parentClassName:                          class childClassName(parentClassName):
            def __init__(self):                             def __init__(self):
                #initialize code                                #initialize code
                                                            
            def objFunc(self):                              def objFunc (self):
                #initialize code                                super().objFunc()
                                                                #Do Something
"""
# #PARENT CLASS
# class Person:
#     def __init__(self, firstName, lastName):
#         self.firstName = firstName
#         self.lastName = lastName

#     def introduce(self):
#         print("I am " + self.firstName + " " + self.lastName)


# #CHILD CLASS
# class Student(Person):
#     def __init__(self, firstName, lastName, course):
#         super().__init__(firstName, lastName)
#         self.course = course

#     def introduce(self):
#         super().introduce()
#         print("my course that I take " + self.course)

# class Employee(Person):
#     def __init__(self, firstName, lastName, salary):
#         super().__init__(firstName, lastName)
#         self.salary = salary

#     def introduce(self):
#         super().introduce()
#         print("The salary of every Teacher in BSIT is " + str(self.salary) + "k")



# person = Person("Lady", "Ada")
# student = Student("Anna", "Bear", "BSIT")
# employee = Employee("Sir", "Hatdog", 100)

# person.introduce()
# student.introduce()
# employee.introduce()

"""
    Adding Function 
        Parent Class                                    Child Class 

        class parentClassName:                          class childClassName(parentClassName):
            def __init__(self):                             def __init__(self):
                #initialize code                                #initialize code
                                                            
            def objFunc(self):                              def objFunc (self):
                #initialize code                                #Do Something
"""
#PARENT CLASS
class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def introduce(self):
        print("I am " + self.firstName + " " + self.lastName)


#CHILD CLASS
class Student(Person):
    def __init__(self, firstName, lastName, course):
        super().__init__(firstName, lastName)
        self.course = course

    def introduce(self):
        super().introduce()
        print("my course that I take " + self.course)

class Employee(Person):
    def __init__(self, firstName, lastName, salary):
        super().__init__(firstName, lastName)
        self.salary = salary

    def introduce(self):
        super().introduce()
        print("The salary of every Teacher in BSIT is " + str(self.salary))

    def saySalary(self):
        print("Salary: " + str(self.salary))



person = Person("Lady", "Ada")
student = Student("Anna", "Bear", "BSIT")
employee = Employee("Sir", "Hatdog", 10000)

person.introduce()
student.introduce()
employee.saySalary()

