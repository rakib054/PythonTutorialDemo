###Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics.

###<<<=====================union() and update(): =====================>>>
#The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities1.union(cities2)   #Create new set of the union of two sets
print("Union :",cities3)

cities1.update(cities2)    # DO union in existing set
print("Union :",cities1)


###<<<============intersection() and intersection_update(): ============>>>
#The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.
cities4 = {"Delhi", "Kabul", "Tokyo","Dhaka", "Singapur", "Berlin", "Seoul", "Madrid"}
cities5 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities6 = cities4.intersection(cities5)   #Create new set of the intersection of two sets
print("Intersection :",cities6)

cities4.intersection_update(cities5)    # DO intersection in existing set
print("Intersection :",cities4)


###<<<==============difference() and difference_update(): ===============>>>
#The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.
cities7 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities8 = {"Seoul", "Kabul", "Madrid", "Delhi"}
cities9 = cities7.difference(cities8)   #Create new set of the difference of two sets
print("Difference :",cities9)

cities7.difference_update(cities8)    # DO difference in existing set
print("Difference :",cities7)


###<<<======symmetric_difference and symmetric_difference_update(): =======>>>
#The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.     /// A symmetric_difference B = (A U B) - (A intersect B)
cities10 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities11 = {"Tokyo", "Madrid", "Seoul", "Delhi"}
cities12 = cities10.symmetric_difference(cities11)   #Create new set of the symmetric_difference of two sets
print("Symmetric-Difference :",cities12)

cities10.symmetric_difference_update(cities11)    # DO symmetric_difference in existing set
print("Symmetric-Difference :",cities10)