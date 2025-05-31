class Animals:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print( f"I am {self.name} and i am {self.age} years old")

    def speak(self):
        print("I don't know what to say")



class Cat(Animals):
    def __init__(self, name, age, color):
        super().__init__(name, age)

        self.color = color
        #self.name = name
        #self.age = age

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old and i am {self.color}")

class Dog(Animals):
    def speak(self):
        print("Bark")

class Fish(Animals):
    pass


a = Animals("Tim", 19)
a.show()
c = Cat("Bill",  18, "Black")
c.show()
d = Dog("kim", 17)
d.show()

