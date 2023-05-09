# class Social_Media:
#     def __init__(self, firstName, lastName, likesCount, friendName):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.likesCount = likesCount
#         self.friendName = friendName

#     def introduce(self):
#         print("Hi I'am " + self.firstName + " " + self.lastName)

#     def fullProfile(self):
#         print("Full Name: " + self.firstName + " " + self.lastName)
#         print("Likes: " , self.likesCount)
#         for name in self.friendName:
#             print("Friends: " + name)

# socialMediaUser = Social_Media("David", "SDPT", 10, friendName=["Alenere SDPT", "Jaymar Catapang", "Joshua Emmanuel Seria"])
# socialMediaUser.introduce()

# socialMediaUser.fullProfile()

class Social_Media:
    def __init__(self, firstName, lastName, likesCount, friendsName):
        self.firstName = firstName
        self.lastName = lastName
        self.likesCount = likesCount
        self.friendsName = friendsName
    
    def introduce(self):
        print("Hi I'am " + self.firstName + " " + self.lastName)
        print()

    def fullProfile(self):
        print("Full Name: " + self.firstName + " " + self.lastName)
        print("Likes    : " + str(self.likesCount))
        print("Friends: ")
        for name in self.friendsName:
            print("   - " + name)

socialMediaUser = Social_Media("David", "SDPT", 10, ["Alenere SDPT", "Jaymar Catapang", "Joshua Emmanuel Seria"])
socialMediaUser.introduce()
socialMediaUser.fullProfile()