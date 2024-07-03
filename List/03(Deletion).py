### .pop() method removes the last item of the list if no index is provided. If an index is provided, then it removes item at that specified index.
colors_01 = ["Red", "Green", "Blue", "Yellow", "Green"]
print(colors_01)
print("After using .pop() method")
colors_01.pop()    # removes the last item of the list
print(colors_01)

colors_01.pop(1)       #removes item at index 1
print(colors_01)


###.reomve() method removes specific item from the list.
colors_02 = ["violet", "indigo", "blue", "green", "yellow"]
print(colors_02)
print("After using .remove() method by removing blue")
colors_02.remove("blue")
print(colors_02)


### del is not a method, rather it is a keyword which deletes item at specific from the list, or deletes the list entirely.
colors_03 = ["yellow", "violet", "blue", "indigo", "green"]
print(colors_03)
print("After using del keyword")
del colors_03[3]    # If given index , act like .pop() method
print(colors_03)
  
try:
    del colors_03    # Otherwize it deletes whole List
    print("List has been deleted.")
    print(colors_03)
except NameError:
    print("As list has been deleted , that list now does not exist anymore.")



### .clear() method clears all items in the list and prints an empty list.
colors_04 = ["violet", "blue", "green", "yellow", "indigo"]
print(colors_04)
print("After using .clear() method")
colors_04.clear()
print(colors_04)