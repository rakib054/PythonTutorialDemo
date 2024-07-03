###Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

###However, we can directly concatenate two tuples instead of converting them to list and back.
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)


###====Unpack Tuples====###
###Unpacking is the process of assigning the tuple items as values to variables.
info = ("Marcus", 20, "MIT")
(name, age, university) = info
print("Name:", name)
print("Age:",age)
print("Studies at:",university)

###You can add an * to one of the variables and depending upon the position of variable and number of items, python matches variables to values and assigns it to the variables.
fauna01 = ("cat", "dog", "horse", "pig", "parrot", "salmon")
(*animals, bird, fish) = fauna01
print("Animals:", animals)
print("Bird:", bird)
print("Fish:", fish)

fauna02 = ("cat", "dog", "horse", "pig", "parrot", "salmon")
(*animals, bird, fish) = fauna02
print("Animals:", animals)
print("Bird:", bird)
print("Fish:", fish)


marks = (2, 3, 9, 6, 4, 9, 5, 9)
print(marks)
print(marks.index(9))
print(marks.index(9, 4, 7))    # .index(element, start, end)
print("The number 9 is here", marks.count(9), "times")