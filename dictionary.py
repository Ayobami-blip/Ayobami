thisdict ={
    "car": "camry",
    "brand": "RX 350",
    "color": ["red", "green", "white"],
    "year": "2005"
}

for car in thisdict:
    print(car, thisdict["car"])

print(thisdict)
print(thisdict['car'])

print(len(thisdict)) # dictionary length

print(type(thisdict))

mydict = dict(
    name = "John",
    level = "part 3",
    department = "CSC"


)
print(mydict)

mydict["level"] = "part 4" # modify keys
print(mydict)

mydict['grade'] = 'A' # add keys and value
print(mydict)

del mydict ["level"] # delete keys and value
print(mydict)

dic = mydict.pop('name') # another way to delete

print(mydict)

for grade in mydict:
    print(grade, mydict[grade])

