#create a simple information of studeny using a dictionary using apply list and nested list and try all method 

studentOneInfo = {
    "compleName" : "Clark Quinn. Davis",
    "age" : 12,
    "gender" : "male",
}

studentsOne = {
    "name" : "Clark Q. Davis",
    "room" : 1,
    "teacher" : "Adams Baker",
    "isEnroll" : True,
    "personalInfo" : studentOneInfo
}

studentsTwo = {
    "name" : "Frank Evans",
    "room" : 1,
    "teacher" : "Adams Baker",
    "isEnroll" : False
}

studentsThree = {
    "name" : "Irwin Jones",
    "room" : 2,
    "teacher" : "Klein Lopez",
    "isEnroll" : True
}

studentsFour = {
    "name" : "Mason Nalty",
    "room" : 3,
    "teacher" : "Ochoa Patel",
    "isEnroll" : True
}

studentsFive = {
    "name" : "Ghosh Hills",
    "room" : 2,
    "teacher" : "Klein Lopez",
    "isEnroll" : False
}

#display studentFive
#print(studentsFive)

#print studentTwo and display the teacher of student
#print(studentsTwo["teacher"])

#add item 
#studentsOne["isActive"] = True
#print(studentsOne)

#store the students that isEnroll in one container name students
students = [studentsOne, studentsThree, studentsFour]
print(students)

#create a nested list 
print(studentsOne.get("personalInfo").get("age"))