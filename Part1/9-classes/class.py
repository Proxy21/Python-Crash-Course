class Dog():
    """A simple dog"""

    def __init__(self, name, age):
        """initializa name age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Dog sitting on command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """simulating rolling over"""
        print(self.name.title() + " rolled over!")




dog1 = Dog('will', 6)
dog2 = Dog("joe", 5)

print("My two dogs names are " + dog1.name.title() + " and " + dog2.name.title())
print("My two dogs are " + str(dog1.age) + " and " + str(dog2.age) + " years old")

dog1.sit()
dog2.roll_over()
