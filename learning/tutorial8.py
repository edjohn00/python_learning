"""
    NESTED FOR Loop - a For Loop inside a For Loop commonly used to iterate throught a multi-dimensional collection

    Using Range in Nested For Loops 
"""
# for x in range(3):
#     for y in range(2):
#         print("Hello")

for x in range(5):
    for y in range(5):
        print("*",end="")
    print("New Line")

"""
    Reading Multi - Dimentional Collections Using Nested For Loops
"""

# batchOne = [
#     ["sectionOne", "John"],
#     ["sectionTwo", "Emman"],
#     ["sectionOne", "Anna"],
#     ["sectionThree", "David"],
#     ["sectionTwo", "Lady"]
# ]

# for section in batchOne:
#     for newBatch in section:
#         print(newBatch)
#     print()