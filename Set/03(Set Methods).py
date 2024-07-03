### isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True. Means , two sets mustn't have any similar element.    /// A intersection B = none!
print("isdisjoint() : ")
# Example1 :
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

print(cities.isdisjoint(cities2))

cities.intersection_update(cities2)    # Just to verify....
print("Because the intersention of two sets are :", cities)


# Example2 :
cities3 = {"Seoul", "Kabul"}
print(cities.isdisjoint(cities3))

cities.intersection_update(cities3)    # Just to verify....
print("Because the intersention of two sets are :", cities)



###issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
print("issuperset() : ")
#Example 1:
cities4 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities5 = {"Seoul", "Kabul"}
print(cities4.issuperset(cities5))
cities6 = {"Seoul", "Madrid","Kabul"}
print(cities4.issuperset(cities6))
 

#Example 2:
cities7 = {"Tokyo", "Madrid"}
print(cities4.issuperset(cities7))



###issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.
print("issubset() : ")
# Example 1:
citie8 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities9 = {"Tokyo", "Madrid"}
print(cities9.issubset(citie8))
 

# Example 2:
cities9 = {"Seoul", "Kabul"}
print(cities9.issubset(citie8))
cities10 = {"Seoul", "Madrid", "Kabul"}
print(cities10.issubset(citie8))