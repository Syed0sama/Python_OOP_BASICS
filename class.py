# Creating a class named DOG
class DOG:

    # Constructor method (runs automatically when object is created)
    def __init__(self, name, age):
        # Store the given name inside the object
        self.name = name
        
        # Store the given age inside the object
        self.age = age

    # Method that returns BOTH name and age as a tuple
    def get_name_age(self):
        return self.name, self.age

    # Method that returns the string "bark"
    def bark(self):
        return "bark"

    # Method that returns the string "eat"
    def eat(self):
        return "eat"

    # Method that returns the string "speak"
    def speak(self):
        return "speak"

    # Method that takes a number c and returns c + 1
    def sum(self, c):
        return c + 1


# Creating first object of DOG class
d = DOG("GOOF", 23)

# Calling bark() method from object d
print(d.bark())      # Output: bark

# Calling eat() method from object d
print(d.eat())       # Output: eat

# Calling speak() method from object d
print(d.speak())     # Output: speak

# Calling sum() method and passing 12 as argument
print(d.sum(12))     # Output: 13


# Creating second object of DOG class
S = DOG("TIM", 32)

# Getting name and age of first object (d)
print(d.get_name_age())  
# Output: ('GOOF', 23)

# Getting name and age of second object (S)
print(S.get_name_age())  
# Output: ('TIM', 32)