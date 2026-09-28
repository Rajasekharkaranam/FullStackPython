#Example: Types of Inheritance
# Single Inheritance
class Animal:
    def eat(self):
        print("Animal eats")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


dog = Dog()
dog.eat()
dog.bark()


# Multilevel Inheritance
class Grandparent:
    def house(self):
        print("Grandparent's house")


class Parent(Grandparent):
    def car(self):
        print("Parent's car")


class Child(Parent):
    def bike(self):
        print("Child's bike")


obj = Child()

obj.house()
obj.car()
obj.bike()
# Multiple Inheritance
class Father:
    def skills1(self):
        print("Driving")


class Mother:
    def skills2(self):
        print("Cooking")


class Child(Father, Mother):
    pass


obj = Child()

obj.skills1()
obj.skills2()