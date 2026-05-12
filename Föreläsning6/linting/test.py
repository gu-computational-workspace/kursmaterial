import os

# Write a class that prints out name and age of a person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_name_age(self):
        print(self.name, self.age)

p = Person("John", 36)


p.print_name_age()


