###Sets are unordered collection of data items. They store multiple items in a single variable. Sets items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.
numbers = {4, 78, 1, 9, 5, 887, 34, 7, 4, 78, 1, 9, 5, 6}
print(numbers)

for value in numbers:
    print(value)

info = {"Carla", 19, False, 5.9, 19}
print(info)
print(type(info))

s = {}    # Pyhton regard empty set as dictionary
print(type(s))

# So you have to define an empty set as set like that
t = set()
print(type(t))

#The error you're encountering, TypeError: 'set' object is not callable, typically occurs when you inadvertently try to call a variable that has been assigned the name of a built-in function or type. In your case, it seems like you've assigned the name set to something else previously in your code, and now when you try to create a new set using set(), it's trying to call whatever set is referring to, rather than creating a new set.

#To resolve this, you can follow these steps:

#Check if set has been assigned: Search your code for any place where you might have used set as a variable name. If you find it, rename that variable to something else to avoid conflicts.
