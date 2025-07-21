class Animal:
    kingdom = "Animalia"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        # Call superclass constructor
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

buddy = Dog("Buddy", "Golden Retriever")
whiskers = Cat("Whiskers")

print(f"{buddy.name} is a {buddy.breed} and belongs to the {buddy.kingdom} kingdom.")
buddy.speak()

print(f"{whiskers.name} belongs to the {whiskers.kingdom} kingdom.")
whiskers.speak()