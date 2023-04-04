# CONDITIONAL STATEMENT

"""
    Conditional Statement - A Statement that makes the program smarter, it makes the program decided on what to do in certain CONDITIONS
    * IF Statement (1 condition)
    * IF-ELSE Statement (2 Condition)
    * IF-ELIF-ELSE Statement (3 or More Conditions)
    * NESTED Conditional Statementes (Condition after a Condition)

    Conditional Operators 
    *  ==   EQUAL
    *  !=   NOT EQUAL
    *  >    GREATER THAN
    *  <    LESS THAN
    *  >=   GREATER THAN OR EQUAL
    *  <=   LESS THAN OR EQUAL

    IDENTATION - is used to Indicate what statements are included inside the Conditional Statement
"""

"""
    IF STATEMENT - used when dealing with ONE Condition
    syntax:                                         example:
    if valueOne > valueTwo                          if age >= 18:
        #do something                                   print("Legal Age")
"""

"""
    IF-ELSE STATEMENT - used when dealing with Two Conditions
    syntax:                                         example:
    if valueOne > valueTwo                          if age >= 18:
        #do something                                   print("Legal Age")
    else:                                           else:
        #do something                                   print("Too Young")
"""

"""
    IF-ELIF-ELSE STATEMENT - used when dealing with THREE OR MORE Conditions
    syntax:                                         example:
    if valueOne > valueTwo                          if age >= 18:
        #do something                                   print("Legal Age")
    elif valueOne >= valueTwo:                      elif age >= 13:
        #do something                                   print("Teenager")
    else:                                           else:
        #do something                                   print("Too Young")
"""

"""
    NESRED CONDITIONAL STATEMENT - used when dealing with CONDITIONS INSIDE A CONDITION
    syntax:
    if valueOne == valueTwo:                        if age >= 18:
        if valueThree == valueFour                      if height >= 170:
            #do something                                   print("Legal Age and Tall)
        elif valueThree                                 elif height >= 156:
            #do something                                   print("Legal Age and Average")
        else:                                           else:
            #do something                                   print("Legal Age and Short")
"""

"""
    LOGICAL OPERATORS - used to include 2 or MORE Condetion in one line 
    * AND - BOTH condition must be true
    * OR - EITHER condition must be true 
"""

"""
    COLLECTION CONDITIONAL STATEMENTS - used to check an item if it's in a collection (list and tuples)
    syntax:                                         example:
    list = [item1, item2, item3]                    bag = ["wallet", "gun", "handkerchirf"]
    if value in list:                               if gun in bag:
        #do something                                   print("Contraband")
    else:                                           else:
        #do something                                   print("All Clear")
"""