#create a simple grading system using if, elif and else
# more than or equal to 98 (with high honor)
# more than or equal to 90 (with honor)
# more than or equal to 75 (passed)
# less than or equal to 74 (fail)

grade = int(input("Enter your grade: "))

if grade > 100 or grade < 0:
    print("Your inputed grade is invalid!!")
elif grade >= 98:
    print("Your average garde is " , grade)
    print("Congrats you are in high honor")
elif grade >= 90:
    print("Your average grade is " , grade)
    print("Congrats your in honor")
elif grade >= 75:
    print("Congrats you are passed this semester, study hard more")
else:
    print("Your failed this semester")

    
