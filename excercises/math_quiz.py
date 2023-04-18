"""
    make a program taht asks a math question the user has 3 chances before he/she loses
"""

# lives = 3 #3chances

# answer = 250 #correct answer

# while lives > 0:
#     question = int(input("100 + 150 = "))
#     if question == answer:
#         print("You Win")
#         break
#     else:
#         lives = lives - 1
# else: 
#     print("You Lose")


#create a 
lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]

my_message=""

message = ""
i = 0
while i < len(lst):
    if lst[i] == 100:
        my_message = "There is a 100 at index no: " + str(i)
    i = i+1



print(my_message)
