#OBJECK FUNCTION

"""
    Object Functions - any function declared inside an object class is considered an Object Function

    Object Functions represent the object's purpose

    Creating & Calling Object Function
    SYNTAX:                                             EXAMPLE: 
        class objectName:                                   class Animal:
            def __init__(self)                                  def __init__(self,type,voice):    
                #initialize code                                    self.type = type
                                                                    self.voice = voice 
            def objectFunc(self)                            
                #do something                                   def speak(self):
                                                                    print(self.voice)
                                                            
                                                            aOne = Animal("Dog","Arf")
                                                            aOne.speak()
"""
# class Animal:
#     def __init__(self, type, voice):
#         self.type = type
#         self.voice = voice
    
#     def speak(self):
#         print(self.voice)

# aOne = Animal("Dog", "Arf")
# aOne.speak()

"""
    Self Parameter 
        - the first parameter of all OBJECT FUNCTIONS is the self parameter it always pertain to the object itself

        - the self parameter name can be chnaged to anything as long as it is the first parameter in the object function
"""
# class Animal:
#     def __init__(self, type, voice):
#         self.type = type
#         self.voice = voice
    
#     def name_of_animal(self):
#         print("I'am a " + self.type)

#     def speak(self):
#         print(self.voice)

# animalOne = Animal("Dog", "Arf")
# animalOne.name_of_animal()
# animalOne.speak()

# animalTwo = Animal("Cat", "Meow")
# animalTwo.name_of_animal()
# animalTwo.speak()

class Students:
    def __init__(self, name, studentId, course, roomNum):
        self.name = name
        self.studentId = studentId
        self.course = course
        self.roomNum = roomNum

    def name_of_student(self):
        print(self.name)

    def student_Id(self):
        print(self.studentId)

    def course_of_student(self):
        print(self.course)

    def student_room(self):
        print(self.roomNum)


studentOne = Students("Seth", 11011, "BSIT", "Room-1")
studentOne.name_of_student()
studentOne.student_Id()
studentOne.course_of_student()
studentOne.student_room()

studentTwo = Students("Daniel", 12011, "BSCS", "Room-2")
studentTwo.name_of_student()
studentTwo.student_Id()
studentTwo.course_of_student()
studentTwo.student_room()


