"""
Assignment 1
"""
# Base Class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def use_power(self):
        print(f"{self.name} uses their generic power: {self.power}")

    def __str__(self):
        return f"{self.name} from {self.origin}, Power: {self.power}"


# Subclasses with unique power usage (Polymorphism)
class Speedster(Superhero):
    def use_power(self):
        print(f"{self.name} runs faster than lightning! ⚡")


class Telepath(Superhero):
    def use_power(self):
        print(f"{self.name} reads and controls minds! 🧠")


class Elemental(Superhero):
    def use_power(self):
        print(f"{self.name} summons fire and wind! 🔥🌪️")

# class/assignment invoker
def super_hero_prompter():
    # Create instances of each subclass
    flash = Speedster("Flash", "Super Speed", "Central City")
    professor_x = Telepath("Professor X", "Telepathy", "Westchester County")
    storm = Elemental("Storm", "Weather Manipulation", "Africa")

    # Store them in a list
    superheroes = [flash, professor_x, storm]

    # Iterate through the list and call use_power on each
    for hero in superheroes:
        hero.use_power()

"""
Assignment 2
"""
# Base class
class Vehicle:
    def move(self):
        print("The vehicle moves in its own way.")

# Subclasses with specific behavior
class Car(Vehicle):
    def move(self):
        print("Driving on the road. 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying through the sky. ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water. 🚢")

# class/assignment invoker
def vehicle_prompter():
    # Create instances of each subclass
    car = Car()
    plane = Plane()
    boat = Boat()

    # Store them in a list
    vehicles = [car, plane, boat]

    # Iterate through the list and call move on each
    for vehicle in vehicles:
        vehicle.move()
