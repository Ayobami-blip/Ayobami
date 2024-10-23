class Animal:
    def sound(self):
        print("Animal makes a sound")

class Animalia(Animal):
    def sound(self):
        print("Animal makes a sound")

class Animan(Animal):
    def sound(self):
        print("Animal makes a sound")

Animal_1 = Animal()
Animal_2 = Animalia()
Animal_3 = Animan()

print(Animal_1.sound())
print(Animal_2.sound())
print(Animal_3.sound())


# Method overloading

class Maths:
    def Add(self,a,b=None):
        if b is None:
            return a
        else:
            return a + b

Addition = Maths()
print(Addition.Add(10))
print(Addition.Add(10,50))