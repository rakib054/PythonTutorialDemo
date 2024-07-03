###If you want to add a single item to the set use the add() method.
a1 = {1, 2, 3}
a1.add(4)
print(a1)

###If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.
a2 = {5, 6, 7}
a1.update(a2)
print(a1) 


###We can use remove() and discard() methods to remove items form list.
a1.remove(7)
print(a1)
a1.discard(6)
print(a1)
#The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.
a1.discard(100)
print(a1)

try:
    a1.remove(100)
    print(a1)
except KeyError:
    print('100 is not present in a1 , so remove() is showing KeyError')



###This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.
a1.pop()
print(a1)


###del is not a method, rather it is a keyword which deletes the set entirely.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
try:
    print(cities)
except NameError:
    print("name 'cities' is not defined/deleted")


###clear() method clears all items in the set and prints an empty set.
cities2 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2.clear()
print(cities2)


###You can also check if an item exists in the set or not.
info = {"Carmen", 19, False, 5.9}
info.discard("Carmen")
if "Carmen" in info:
    print("Carmen is present.")
else:
    print("Carmen is absent.")