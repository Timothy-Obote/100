#Python Object Oriented Programming
class Dog:

    def __init__(self, name, age):
        self.name = name #attribute of class Dog which is name
        self.age = age
        print(name)

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d = Dog("Tim" , 34)
#print(d.name)
d.set_age(23)
print(d.get_age())



#d2 = Dog("Bill")
#print(d2.name)


#d.bark()
#print(d.add_one(5))
#print(type(d))