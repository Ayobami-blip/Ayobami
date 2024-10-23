my_list = ['1', '2', '3', '4']
print(my_list[0])

my_list[1]= 5  # modifying with index number
print(my_list)

my_list.append(7) # adding one item
print(my_list)

my_list.insert(2, 9) # replacing a word with index(the first one)
print(my_list)

my_list.extend([3, 4, 7]) # adding numerous items
print(my_list)

my_list.remove(9)
print(my_list)


slicer = my_list[0 : 4] # keeps only integers within the range of the index assigned
print(slicer)

print(len(my_list))

my_list1 = [6 , 7, 8, 9]

my_list3 = my_list + my_list1

print(my_list3)