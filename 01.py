###Data Types

# list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print("List : " , list1)
for i in list1 :
    print(i)

# tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print("Tuple : ",tuple1)
for i in tuple1 :
    print(i)

#dict: a dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print("Dictionary : " , dict1)
for i in dict1 :
    print(i)

# Set is an unordered collection of elements in which no element is repeated. The elements of sets are separated by a comma and contained within curly braces.
set1 = {4, -5, 8, 3, 2.9}
print("Set : " , set1)
for i in set1 :
    print(i)

#range: returns a sequence of numbers as specified by the user. If not specified by the user then it starts from 0 by default and increments by 1.

print("Here are some odd numbers using range()")
sequence1 = range(1,13,2)   #range(Start , End , Diff)
for i in sequence1:
    print(i)

###Types
a = 7
b = 3.3
c = 2 + 5j
d = "I'm Rakib"
print(type(a))
print(type(b))
print(type(c))
print(type(d))

