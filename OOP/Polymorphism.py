class Vehicle:
    def intro(self):
        return "Every vehicle can move"

    def how(self):
        return "Most of the time use wheels to move"

class Car(Vehicle):
    def how(self):
        return "Use Wheels to move"

class Plane(Vehicle):
    def how(self):
        return "Use wings to move"

veh = Vehicle()
car = Car()
plane = Plane()

print(f"{veh.intro()} and vehicle {veh.how()}")
print(f"{car.intro()} and Car {car.how()}")
print(f"{plane.intro()} and Plane {plane.how()}")