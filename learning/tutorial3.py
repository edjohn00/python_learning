# Sets | sets functions
'''
    Sets - a collection of Variables that is Partially Writable and it's unordered and unindexed
    syntax: identifier = {value1, value2, value3}
    names_of_persons = {"john", "joey", "jorge"}

    Reading WHOLE Sets - you can read a set by printing the whole set
    syntax: print(set)
'''
evenNumbers = {0, 2, 4, 6, 8, 10}
print(evenNumbers)

'''
    Reading Set ITEMS - Its is not possible to read certain item in a set unless you cast it into a List ot Tuple
    hence Sets are unindexed and unordered

    Set LENGTH - you can check the number of items in a set buy using len() function
    syntax: len(set)

    Set ADD ITEMS - you can add items in set by using add() and it will be add at the END OF THE SET
    syntax: set.add(value)
    numbers.add()

    Set ADD MULTIPLE ITEMS - you can add multiple item in the set by using uppdate()
    syntax: set.update(list)
    number.update([7,8,9,10])

    Set Deleting Items by remove() - you can deletes an item based on their value | if the value doesn't exist in the set it will be counted as an ERROR
    syntax: set.remove(value)
    number.remove(1)

    Set Deleting Items by discard() - same to remove it will delete based on their value but | if the value doesn't exist in the set it will not ERROR
    syntax: set.discard(value)
    numbers.discard(1)

    Set Deleting Items by pop() - delete the first item in the set 
    syntax: set.pop()

    Set Deleting Items by clear() - delete all the value in set | notes: that delete the set variable 
    syntax: set.clear() 
'''
print(len(evenNumbers)) #len()

evenNumbers.add(12) # add()
print(evenNumbers)

setUpdate = [14, 16, 18, 20] # setUpdate is storage variable 
evenNumbers.update(setUpdate) # update()
print(evenNumbers)

evenNumbers.remove(20) #remove()
print(evenNumbers)

evenNumbers.discard(22) #discard()
print(evenNumbers)

evenNumbers.pop() #pop()
print(evenNumbers)

evenNumbers.clear()
print(evenNumbers)

'''
    Copying Set - copies the whole set ehich can assigned to new set using copy()
    syntax: setOne = {1, 2, 3, 4, 5}
            setTwo = setOne.copy()

    Union Set - - return a set containing all the values of the two sets
    syntax: setOne = {1, 2, 3, 4, 5}
            setTwo = {6, 7, 8 , 9}
            setThree = setOne.union(setTwo)

    Difference Set - return a set containing the values that only exist on the left set and not on the right set
    syntax: setOne = {1, 2, 3, 4, 5}
            setTwo = {1, 2, 3}
            setThree = setOne.difference(setTwo)

    Intersection Set - return a set containing the values that exist both on the two sets
    syntax: setOne = {1, 2, 3, 4, 5}
            setTwo = {1, 2, 3}
            setThree = setOne.intersection(setTwo)

    Symmetric Difference Set - return a set containing all values that exists exclusively on each set
    syntax: setOne = {1, 2, 3, 4, 5}
            setTwo = {1, 2, 3}
            setThree = setOne.symmetic_difference(setTwo)

    Disjoint Set - returns a boolean whether two sets have an intersection or not 
    syntax: setOne.isdisjoint(twoset)

    Subset - returns a boolean whether the left set is contained in the right set
    syntax: setOne.issubset(setTwo)

    Superset - returns a boolean whether the right set is contained in the left se
    syntax: setOne.issuperset(settwo)

'''
# copy()
numbers_one = {1, 2, 3, 4, 5} 
numbers_two = numbers_one.copy() #copy()
print(numbers_two)

# union()
fruits = {"apple", "cheery", "banana"}
vegetable = {"gabbage", "eggplant", "potato"}
healthyFoods = fruits.union(vegetable) 
print(healthyFoods)

# difference
setOne = {2, 8, 4, 5, 3, 1}
setTwo = {3, 5, 6, 9, 8}
setThree = setOne.difference(setTwo)
print(setThree)

# intersection
setThree = setOne.intersection(setTwo)
print(setThree)

# symmetric difference
setThree = setOne.symmetric_difference(setTwo)
print(setThree)

# disjoint
fruits = {"apple", "cheery", "banana"}
vegetable = {"gabbage", "eggplant", "potato", "apple"}
print(healthyFoods.isdisjoint(vegetable))

# subset
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
evenNumbers = {2, 4, 6, 8, 10}
print(evenNumbers.issubset(numbers))

# superset
print(evenNumbers.issuperset(numbers))

'''
    Casting Sets - you can cast Sets to Turples or List VICEVERSA in the same way you cast other variables
'''
dataTypes = {"String", "List", "Boolean",{"John", "Deo", "Ken"}}
print(dataTypes)




