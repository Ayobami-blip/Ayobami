import random
u = random.randint(10,20)
print(u)
x = random.uniform(10,100)
print(x)


from math import *
i = pow(3,3)
print(i)
o = sin(30)
print(o)

cars = ['Toyota', 'Benz', 'BMW']
cars.append('kkkkk')
cars.remove('BMW')
cars.pop(2)

print(cars)


# print(cars[-1])
# print(cars[-2])
# print(len(cars))
# print(cars.append('jjjjjj'))


# for i in cars:
#     print(i)

# functions

# def rat(fname, lname):
#      print(fname + " " + lname)
# rat('David', 'Umukoro')

def rat(*fname):
     print('My first name is ' + fname[0])
rat('David', 'Umukoro', 'Umukoro', 'Sunday', 'Quadri')

def name (child1 , child2 , child3):
     print( "My name is " + child3)
name (child1 = "John", child2 = "Joan", child3 = "Kelly") 

def rat (**kids):
     print('His last name is ' + kids['lname'] )
rat(fname = 'dog', lname = 'fish')     

def myfunction(food):
     for x in food:
          print(x)

fruits = ['apple', 'mango', 'orange']
myfunction(fruits)

#class in py

class part_1():
    def __init__(davi, number, age):
         davi.num = number
         davi.ag = age
    def got(abc):
         print('My number is ' + abc.num + ' My age is ' + abc.ag)

x = part_1('89', '90')
print(x.got())
# print(x.num)
 


# class Banking(): 
#     def __init__(self, number, balance = 0.0, withdraw = 0.0):
#           self.number = number
#           self.balance = balance
#           self.withdraw = withdraw
     

#     def deposit(self):            
#             print('You deposited $', self.number, ' .My Balance is ', self.number)
     
#     def withdraw(self):
#           print("You've withdrawn ")


# x = Banking(input('How much do you want to deposit: '))
# print(x.deposit())
# y = Banking(input('How much do you want to withdraw: '))
# print(x.withdraw())

from classs import emp
poly = emp()
print(poly.age)