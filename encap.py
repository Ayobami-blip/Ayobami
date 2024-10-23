class myClass():
    def set_age(self, age):
        self.age = age

    def output(self):
        return self.age

y = myClass()
y.set_age(10)
print(y.output())


class myClass():
    def set_age(self, age):
        if isinstance(age,(int,float,str,complex)):
            self.age = age
        else:
            raise ValueError('not valid')

    def get_age(self):
        return(self.age)

x = myClass()
x.set_age(20j)
print(x.get_age())






# instance attribute
class myclass():

    def __init__(self, age , name):
        self.age = age
        self.name = name
x = myclass(9 , "ada")
print(x.age , x.name)

# class attribute
class attr():
    car = "Lexus"
    model = "350"

# def __init__ (self, watch):
#     self.watch = watch

# x = attr("rolex")
# print(x.watch)
v = attr()
print(v.car , v.model)

