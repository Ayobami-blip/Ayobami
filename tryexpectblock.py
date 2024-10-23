# try:
#     numerator = 10
#     denominator = 0
#     result = numerator/denominator
#     print(result)
# except:
#     ZeroDivisionError
#     print('Number is infinity')

# try: 
#     from name import *
# except:
#     ModuleNotFoundError
#     print('Page not found')


def divide (x, y):
    assert y!=0 #
    return x/y
try: 
    print(divide(10,0))
except AssertionError as e:
    print(f'Assertion failed')

# Key error
thisdict = {
    "cars": "lexus",
    "color": "red"
}
try:
    print(thisdict[2])
except:
    KeyError
    print('Key is not in the dictionary')
