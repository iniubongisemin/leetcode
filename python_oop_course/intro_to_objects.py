name = "Inie"
age = 29

# print(type(name))
# print(type(age))

class Dog:
    def bark(self):
        print("Whoof whoof!!!")

bingo = Dog()
# bingo.bark()

# Attributes/Data Fields in a Class
# >> Define and init method
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Whoof whoof!!!")
# PS: The __init__ method is run only once when the object is instantiated
# Items like self.name in the init method are called datafields
# Class: Blueprint for creating objects 
# Object: Intance of a class
# Attributes: Variables that store information about an object
# Methods: Functions inside a class that define what the class can do
# self: Refers a specific object of a class itself

# When you you create an instance of a class, you are instantiating the class! 

class Owner:
    def __init__(self, name, address, phone_no):
        self.name = name
        self.address = address
        self.contact_number = phone_no

owner_one = Owner(name="Ini-ubong", address="6 Adebambo close, Obanikoro, Lagos", phone_no="08101859094")


dog_one = Dog("Bingo", "German shepherd", owner=owner_one)
# print(dog_one.name)
# print(dog_one.breed)
# print("Dog Owner:", dog_one.owner.name)
# dog_one.bark()

dog_two = Dog("Freya", "Belgian malinois", owner=owner_one)
# print(dog_two.name)
# print(dog_two.breed)
# print("Dog Owner:", dog_one.owner.name)
# dog_two.bark()


# Example_two
class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def greet(self):
        print(f"Hello there, my name is {self.name} and I am a {self.occupation} 😎. I am {self.age} years old")


person_one = Person("Ini-ubong", 27, "Software Engineer")
person_one.greet()

person_two = Person("Eugene", 27, "Backend Engineer")
person_two.greet()
