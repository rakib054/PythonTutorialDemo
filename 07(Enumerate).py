marks = [12, 45,11, 75, 34]

for i in marks:
    print(i)
    if i==11:
        print("Not Good")    # No way to identify index

print("\n\n")

# You can use index using enumerate()
for index , mark in enumerate(marks):
    print(f"{index} No. is {mark}")
    if index == 2:
        print("Not Good")

print("\n\n")

# You can also start index from 1(instead of 0)
for index, mark in enumerate(marks,start = 1):
    print(f"{index} No. is {mark}")