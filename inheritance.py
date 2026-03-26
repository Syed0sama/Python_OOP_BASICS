# Parent class PET (Base class)
class PET:
    # Constructor method to initialize name and age
    def __init__(self, name, age):
        self.name = name  # store pet's name
        self.age = age    # store pet's age

    # Method to show pet details
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    # Default speak method for any PET
    def speak(self):
        print("I don't know what I say")


# Child class cat inheriting from PET
class cat(PET):
    # Constructor for cat
    def __init__(self, name, age, color):
        # Call the parent constructor to set name and age
        super().__init__(name, age)
        self.color = color  # additional attribute specific to cat

    # Overriding the show() method of parent PET
    def show(self):
        # Prints name, age, and color
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}.")

    # Overriding the speak() method of parent PET
    def speak(self):
        print("MEAWWOO")


# Child class dog inheriting from PET
class dog(PET):
    # Inherits __init__ and show() from PET (no need to redefine)
    
    # Overriding the speak() method
    def speak(self):
        print("BHAO BHAO")


# Child class fish inheriting from PET
class fish(PET):
    # No methods defined → inherits everything from PET
    pass  # "pass" means we don’t add anything new here


# Creating objects of different classes and calling methods

# Creating a generic PET object
p = PET('billo', 26)
p.show()       # Calls PET.show() → "I am billo and I am 26 years old"
p.speak()      # Calls PET.speak() → "I don't know what I say"

# Creating a cat object
c = cat('Mano', 14, 'White')
c.show()       # Calls cat.show() → overrides PET.show()
c.speak()      # Calls cat.speak() → overrides PET.speak()

# Creating a dog object
d = dog('tommy', 32)
d.show()       # Calls PET.show() → inherited from PET
d.speak()      # Calls dog.speak() → overrides PET.speak()

# Creating a fish object
f = fish('jal ki rani', 4)
f.show()       # Calls PET.show() → inherited from PET
f.speak()      # Calls PET.speak() → inherited from PET