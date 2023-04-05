"""
    GRADE AVERAGE PROGRAM - create a program that makes the user input 3 grades so that the system could average it then check if the grades is: 

    > 100 OR <= 50 ~ Invalid Grade
      98 - 100     ~ With Highest Honor
      95 - 97      ~ With High Honor 
      90 - 94      ~ With Honors
      75 - 89      ~ Passed 
      74 - 51      ~ Failed

    PS: Print the necessary message for each condition
"""
Filipino = float(input("Enter a grade in Filipino: "))
English = float(input("Enter a grade in English: "))
Math = float(input("Enter a grade in Math: "))
Science = float(input("Enter a grade in Science: "))
Programming = float(input("Enter a grade Programming: "))

student_average = (Filipino + English + Math + Science + Programming) / 5

if student_average > 100 or student_average <= 50:
    print("Your grades is invalid")
elif student_average >= 98:
    print("Your With Highest Honor")
    print("Congratulation")
elif student_average >= 95:
    print("Your With High Honor")
elif student_average >= 90:
    print("Your With Honor")
elif student_average >= 75:
    print("Your Passed, Study more to get a higher grade")
else:
    print("You failed this semister")