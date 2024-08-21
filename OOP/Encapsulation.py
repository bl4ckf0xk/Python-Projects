class Car:
    behaviour = "move"

    def __init__(self, name, model, color):
        self.name = name
        self._model = model
        self._color = color

    def wht_color(self):
        print(f"{self.name} color is {self._color}")

    def wht_model(self):
        print(f"{self.name} model is {self._model}")

    def get_color(self):
        return self._color
    
    def chng_color(self, new_color):
        self._color = new_color

Nex = Car("whtNex", "benz", "white")
# print(Nex.wht_color()) # not recommended coz it's a private attr
# print(Nex.wht_model())

print(Nex.get_color())
Nex.chng_color("Red")
print(Nex.get_color())
