# public

# class Employee:
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         print(f'{self.name}, {self.age}')
    
# name = Employee("John", 10)

# name.display()

# private

class Employee:
    def __init__ (self, name, age):
        self._name = name
        self._age = age
    
    def display(self):
        print(f'{self._name}, {self._age}')
    
name = Employee("John", 10)

# name.display()

class Person(Employee):
    def __init__(self, name, age, number):
        super().__init__(name, age)
        self.number = number

    def Person_Details(self):
            print(f"{self._name},{self._age},{self.number}")

person = Person('John', 29, 987654321)
person.Person_Details()
        # protected

# class Employee:
#     def __init__ (self, name, age):
#         self.__name = name
#         self.__age = age
    
#     def display(self):
#         print(f'{self.__name}, {self.__age}')
    
# name = Employee("John", 10)

# name.display()
