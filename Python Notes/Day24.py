#Example 1: Operator Polymorphism
print(10 + 20)

print("Python " + "Full Stack")

print([1, 2] + [3, 4])
#Example 2: Method Overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()