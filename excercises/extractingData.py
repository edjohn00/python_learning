"""
    Extracting the Data

    Given the Collection:
    student = [["BSIT",["David", "Alenere"]], ["BSCS", ["Jaymar", "Emman", "Patricl"]]]

    Print them in a wat that you will Distinguish who are the BSIT and BSCS

    Possible Output:

    BSIT
        David
        Alenere

    BSCS
        Jaymar
        Emman
        Patrick
"""

# course = [
#     ["BSIT", ["David", "Allenere"]],
#     ["BSCS", ["Jaymar", "Emman", "Patrick"]]
# ]

# for student in course:
#     for newStudent in student:
#         print(newStudent)
#     print()


course = [      
    ["BSIT", ["David", "Allenere"]],
    ["BSCS", ["Jaymar", "Emman", "Patrick"]]
]

# for newCourse in course:
#     print(newCourse[0])
#     for student in newCourse[1]:
#         print("   -" + student)
#     print()

# for newCourse in range(course):
#     for student in range(newCourse):
#         print(course[newCourse][student])

for newCourse in course:
    print(newCourse[0])
    for student in newCourse[1]:
        print(student)