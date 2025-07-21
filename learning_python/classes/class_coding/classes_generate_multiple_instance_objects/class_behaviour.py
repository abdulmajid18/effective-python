class Animal:
    # Class attribute (shared across all instances)
    kingdom = 'Animalia'

    def __init__(self, name, species):
        # Instance attributes (specific to each object)
        self.name = name
        self.species = species

    def speak(self):
        print(f"{self.name} says hello!")

    def info(self):
        print(f"{self.name} is a {self.species} and belongs to the {Animal.kingdom} kingdom.")

# The class statement is executed when the file runs or is imported,
# and now Animal is a class object.


print("Class attribute:", Animal.kingdom)

# Creating instances (objects) of the class
dog = Animal("Buddy", "Dog")
cat = Animal("Whiskers", "Cat")

# Accessing instance methods and attributes
dog.speak()
cat.speak()

# Access class-level and instance-level data
dog.info()
cat.info()
