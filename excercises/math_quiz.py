"""
    make a program taht asks a math question the user has 3 chances before he/she loses
"""

lives = 3 #3chances

answer = 250 #correct answer

while lives > 0:
    question = int(input("100 + 150 = "))
    if question == answer:
        print("You Win")
        break
    else:
        lives = lives - 1
else: 
    print("You Lose")