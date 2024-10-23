class Fun():
     name = "go"
     def greet(self):
           print(self.name)

x = Fun()
print(x.greet())

class emp():
    def __init__(self):
        self.age = 10
    def emp_id(self):
        print(1)
x = emp()
print(x.age)

class myClass():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display (self):
        print(f'name: {self.name}, age: {self.age}')


class1 = myClass("Quadri", 10)
class1.display()

class1.display()

class obj():
    pass

class2 = obj()
print(class2)
class2 = obj()
print(class2)



class obj():
    var =20
    print(var)
    def me(self):
        print('hellox')


