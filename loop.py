cars = ('Toyota', 'Benz', 'GLK')

for x in cars:
    print(x)

for number in range(1,3):
    print(number)

for index,cars in enumerate(cars):
    print(f"index{index}, cars{cars}")

# x = 0
# while x < 5:
#     print(x)
#     if x == 3:
#         break
#     x+=1 # increment in python

x = 1
while x < 6:
    x+=1
    if x == 3:
        continue
    print(x)

x = 0
while x < 3:
    if x % 2 == 0:
        print(f"{x} is an even number")
    else:
        print(f'{x} is an odd number')
    x+=1

    
       
   