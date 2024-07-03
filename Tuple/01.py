###Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable/immutable meaning we can not alter them after creation.
tup = (1, 4, 8, 4, 8, 0)
print(type(tup), tup)

tup2 = ()
print(type(tup2), tup2)

tup3 = (1)    # If one element is present in tuple , it will be regarded as "int"/"string" datatype , not Tuple
print(type(tup3), tup3)

tup4 = (1,)    # So , in this case , use "," after that element
print(type(tup4), tup4)

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])

country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")

