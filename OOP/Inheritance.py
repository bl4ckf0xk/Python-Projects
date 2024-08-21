# class Parent:
#     hair_color = "white",
#     speaks = ['English']

# class Child(Parent):
#     pass

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.speaks.append("German")

# print(Child.hair_color , Child.speaks)
# print(Parent.hair_color , Parent.speaks)

class Dog:
    species = "Canis"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speaks(self, sound):
        return f"{self.name} says {sound}"
    
class Jack(Dog):
    def speaks(self, sound = "Arf"):
        return f"{self.name} says {sound}"

class Dach(Dog):
    def speaks(self, sound = "bah"):
        return f"{self.name} says {sound}"

class Bull(Dog):
    def speaks(self, sound = "yah"):
        return f"{self.name} says {sound}"
    

bull = Bull("kall", 5)
print(bull.speaks())