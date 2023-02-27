#Function is a block of code with only runs when it's called also can return dtas as a results
#in python a function is defined using the def keyword
#to call a function, use the function name followed by parenthesis:
def function_name(): 
    print("this is a function")
function_name()
#one thing to remember, when you create a function we need to define a function first before we can call it

#Arguments are specified after the function name, inside the parentheses. 
#the following example has a function with one argument (name)
def greeting(name):
    print("Hi my name is " + name) 
greeting("John") #john is the varable called "name"

#You can add as many arguments as you want, just separate them with a comma.
#The following example has a function with more one argument
def persons_name(name1, name2, name3):
    print("name1: " + name1)
    print("name2: " + name2)
    print("name3: " + name3)
persons_name("Anna", "Ken", "Jana")

def best_album(album1, album2, album3):
    print("this is the best song of Taylor's Album: ")
    print("From Album: " + album1 + ", " + album2 + ", " + album3)
best_album("Red", "Lover", "Evermore")

#you can also create a user input type in fuction
def person_info(name, age, address):
    print("Hi my name is " + name + " I am " + age + " yrs old and live in " + address )
name = input("Your Name: ")
age = input("Your Age: ")
address = input("Your Address: ")
person_info(name, age, address)