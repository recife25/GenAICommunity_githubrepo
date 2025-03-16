class Animal:
    def __init__(self, name):
        self.name = name 

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed 

    def speak(self):
        return f"{self.name} says woof"
        # Create an instance of Dog

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return f"{self.name} says meow"
        # Create an instance of Cat

dog = Dog("Buddy", "Golden Retriever")  
cat = Cat("Whiskers", "Black")
print(dog.speak())  # Output: Buddy says woof
print(cat.speak())  # Output: Whiskers says meow

