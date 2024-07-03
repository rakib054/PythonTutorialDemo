### Changing items from list is easier, you just have to specify the index where you want to replace the item with existing item.
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
# Index :   0        1        2        3       4
print(names)
print("Change Sarah to Millie")
names[1] = "Millie"    # "Sarah" has been changed to "Millie"
print(names)

print("\n")

### You can also change more than a single item at once. To do this, just specify the index range over which you want to change the items.
print("Change Nadia and Oleg into Juan and Anastasia")
names[2:4] = ["Juan", "Anastasia"]    # [2:4] ==  ["Nadia", "Oleg"]  (Changed to)==>  ["Juan", "Anastasia"]
print(names)


print("\n\n")


### What if the range of the index is more than the list of items provided?
### In this case, all the items within the index range of the original list are replaced by the items that are provided.
names2 = ["Sarah", "Steve", "Oleg", "Harry", "Nadia"]
print(names2)
print("Presenting more changes in List")
names2[1:4] = ["Juan", "Anastasia"]    # [1:4] ==  ["Steve", "Oleg", "Harry", "Nadia"]  (Changed to)==>  ["Juan", "Anastasia"]
print(names2)

print("\n")

names3 = ["Nadia", "Oleg", "Harry", "Sarah", "Steve"]
print(names3)
print("Presenting furthur more changes in List")
names3[2:3] = ["Juan", "Anastasia", "Bruno", "Olga", "Rosa"]    # [2:3] ==  ["Harry", "Sarah"]  (Changed to)==>  ["Juan", "Anastasia", "Bruno", "Olga", "Rosa"]
print(names3)