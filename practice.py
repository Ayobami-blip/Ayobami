# u = 'Hello world'
# print(u)
# x = str('3')
# print(x)
# x , y, z = "orange", "cherry", "banana"
# print(x)

# fruits = ["Banana", "Cherry", "Mango"]
# x , y , z = fruits
# print(x)
# print(fruits)
# print(type(fruits))

# x = 'MEE'
# y = 'MTH'
# z = 'CSC'
# print(x , y , z)
# print(x + y + z)
# print(type(x))

# courses = ('MTH', 'CSC', 'MEE')
# print(type(courses))

# thisdict = {
#     "brand" : "ford",
#     "model" : "Mustang" ,
#     "year" : 1964
# }
# print(thisdict)

# class fun():
#     name = "go"
#     number = 10
#     def greet(self):
#         print(self.number)
#     def gb(self):
#         print(self.name)

# x = fun()
# print(x.greet()) 
# print(x.gb())       

# class ep():
#     def __init__(self, number, name):
#         self.number = number
#         self.name = name

#     def output(self):
#         print(f"{self.number}, {self.name}")

# myinfo = ep(10, "Ade")
# myinfo.output()


# class practice():
#     car = "ferrari"

# def __init__(self, name, model):
#     self.name = name
#     self.model = model

# x = practice("car", "jet")
# print(x.name, x.model)

# from abc import ABC, abstractmethod

# class grade(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass

# class credit(grade):
#     def start(self):
#         return "Distinction"    
#     def stop(self):
#         return "Passed"



# def result(Credit:credit):
#     # if grade > 7:
#     print(Credit.start())
#     # else:
#     print(Credit.stop())

# exam = credit()
# result(exam)

class Employee:
    def __init__(self,name,age):
        self._age = age
        self._name = name
    
    def display(self):
        print(f'{self._name}, {self._age}')

name = Employee('SAAD', 10)

name.display()

class password:
    def __init__(self,name):
        self.name = name
    
    def main():
        pass

def david():
    password = input('Enter your password: ')
    message = main()
    
david()
        
    






