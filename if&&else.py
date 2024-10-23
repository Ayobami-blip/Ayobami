x = -5
if x > 0:
    print('Postive integer')
elif x < 0:
    print('Negative integer')
else:
    print('number is 0')


# nested if
x = 5
if x > 2 :
    print('This is true')
    if x > 3 :
        print('This is also true')
    else:
        print('This is not true')
else: 
        print('This is also not true')


score = 85
if score >= 50:
    print('You passed the exam')

    if score >= 90:
        print('You passed with distinction')
    else:
        print('Good job, but no distinction')
else:
    print('You failed the exam')


cars = ('Toyota', 'Benz', 'GLK')

for x in cars:
    print(x)