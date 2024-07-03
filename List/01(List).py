marks = [5, 6, 4, 8, 3, 9]
print(type(marks) , "Which contains datasets in 3rd Braket and it is mutable/changable")

if 4 in marks:
    print('Yes')

# Same thing is also applied for String
name = "Rakib"
if "ak" in name:
    print('Yes')
else:
    print('No')

if "akb" in name:   # 'Rakib' contain 'akib' , not 'akb'
    print('Yes')
else:
    print('No')


list_01 = [i for i in range(5)]    # You can add for loop to do anything
print(list_01)

list_02 = [i*i for i in range(5)]    # More usage of loo[]
print(list_02)

list_03 = [i*i for i in range(5) if i%2==0]    # ALso add condition
print(list_03)


names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
print(names)
names_With_o = [item for item in names if "o" in item]
print(names_With_o)

names_With_More_Than_Four_Letter = [item for item in names if (len(item) > 4)]
print(names_With_More_Than_Four_Letter)