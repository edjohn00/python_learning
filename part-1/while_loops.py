#while loop we can execute a set of statements as long as a condition is true.

# count = 5

# while count <=  10:
#     print(count)
#     count = count + 1

# add = int(input("Enter a number: "))

# count_num = 1
# while count_num < 5:
#     result_add = add + count_num
#     print(add, "+", count_num, "=", result_add)
#     count_num = count_num + 1


# number = int(input("Enter a number: "))


age = int(input("Enter Your Age: "))

while age < 18:
    print("You are still young ", age)
    age = age + 1
else:
    print("You are in Legal Age ", age)