class Dog:
    species = "German"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    # Same as description but more useful
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"

bike = Dog("bike", 2)
mike = Dog("mike", 5)

print("First dog name is:",bike.name ,"and age is:",bike.age)
print("Second dog name is:",mike.name ,"and age is:",mike.age)
print("First dog species is:",bike.species,"and Second dog species is:",mike.species)
print("----------------------")
print("Mikes' Description:",mike.description())
print("Str is:",mike)
print(mike.speak("Woof Woof"))