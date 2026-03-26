# Creating a class Person
class Person:

    # Class variable → shared by all instances
    number_of_people = 0

    # Constructor method → runs whenever a new object is created
    def __init__(self, name):
        self.name = name   # Instance variable → unique for each object

        # Call the class method add_person() to increase number_of_people
        Person.add_person()   # Or could use: type(self).add_person()


    # Class method to return the current number of people
    @classmethod
    def number_of_people_(cls):
        # cls → refers to the class itself (Person)
        return cls.number_of_people

    # Class method to increment the number_of_people counter
    @classmethod
    def add_person(cls):
        # Increment the class variable by 1
        cls.number_of_people += 1


# Creating first Person object
p1 = Person("Osama")

# Print the class variable directly from the class
print(Person.number_of_people)   # Output: 1

# Creating second Person object
p2 = Person("Nouman")

# Print the class variable again
print(Person.number_of_people)   # Output: 2

# Using class method to get the number of people
print(Person.number_of_people_())   # Output: 2