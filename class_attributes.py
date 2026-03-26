# Creating a class named Person
class Person:

    # This is a CLASS VARIABLE
    # It belongs to the class itself (shared by all objects)
    number_of_people = 0

    # Constructor method (runs when object is created)
    def __init__(self, name):
        self.name = name   # Instance variable (belongs to each object)

        # Increase class variable every time a new object is created
        Person.number_of_people += 1


# Creating first object
p1 = Person("Osama")

# Printing class variable
print(Person.number_of_people)   # Output: 1


# Creating second object
p2 = Person("Nouman")

# Printing class variable again
print(Person.number_of_people)   # Output: 2