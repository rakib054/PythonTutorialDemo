###There are two ways to add items to a dictionary.
# 1.Create a new key and assign a value to it:
info1 = {'name':'Karan', 'age':19, 'eligible':True}
print(info1)
info1['DOB'] = 2001
print(info1)

#We can use the copy() method to copy the contents of one dictionary into another dictionary.
newDictionary1 = info1.copy()
print("Copied dictionary :",newDictionary1)

#Or we can use the dict() function to make a new dictionary with the items of original dictionary.
newDictionary2 = dict(info1)
print("Copied dictionary :",newDictionary2)


# 2.Use the update() method:
#The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
info2 = {'name':'Karan', 'age':19, 'eligible':True}
print(info2)
info2.update({'age':20})
info2.update({'DOB':2001})
print(info2)

info3 = {'id':14534, 'position':'Manager', 'gender':'male'}
info2.update(info3)
print(info2)


### pop() method removes the key-value pair whose key is passed as a parameter.
info2.pop('DOB')
print(info2)

### popitem() method removes the last key-value pair from the dictionary.
info2.popitem()
print(info2)

### clear(): The clear() method removes all the items from the list. 
info2.clear()
print("Dictionary is cleared using clear() method")
print(info2)


### Apart from these four methods, we can also use the del keyword to remove a dictionary item. 
del info1
try:
    print(info1)
except NameError:
    print("name 'info' is not defined/deleted")