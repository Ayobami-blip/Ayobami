# class employee: 
#     raise_percentage = 5

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def apply_raise(self):
#         amount = (self.salary * employee.raise_percentage)/100
#         self.salary +=amount
#         return self.salary


# person1 = employee('John', 5000)
# person2 = employee('Joan', 4000)

# print(f"{person1.name}, {person1.salary}")
# print(f"{person2.name}, {person2.salary}")

# person1.apply_raise()
# print(f"After raise: {person1.name}, {person1.salary}")
# print(f"After raise: {person2.name}, {person2.salary}")


# raise_percentage = 10

# person1.apply_raise()
# person2.apply_raise()
# print(f"After raise: {person1.name}, {person1.salary}")
# print(f"After raise: {person2.name}, {person2.salary}")


# Parent name
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

# Child class
class Employee(Person):
    def __init__(self, first_name, last_name, employee_id):
        super().__init__(first_name, last_name)
        self.employee_id = employee_id

    def employee_details(self):
        return f"{self.full_name()}, {self.employee_id}"


employee1 = Person('Mark', "John")
employee2 = Employee("John", "Doe", 2)
print(employee1.full_name())
print(employee2.employee_details())


    