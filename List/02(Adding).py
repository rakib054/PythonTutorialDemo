l=(17,18)
list_03 = [i*i for i in range(5) if i%2==0]
print(list_03)
list_03.append(17)    # add data at the end of the list
print(list_03)
# but you can't add multiple datas. You can add tuple , list ,... but they would be shown as different data-type

t=(18 , 19 , 20)
list_03.extend(t)    # But worry not , you can use .extend() to solve the problem
print(list_03)
new_list = [21, 22, 25]
list_04 = list_03 + new_list    # You can also extend without changing main List by adding "+" , like this . But it only applies for list datatypes
print(list_04)

marks = [5, 6, 4, 8, 3, 9]
print(marks)
marks.sort()
print(marks)    # Sort out numbers in list , but list is also changesd
marks.reverse()
print(marks)
marks.sort(reverse=True)    # .reverse() and .sort(reverse=True) are same in action
print(marks)
colors = ['violet' , 'yellow' , 'green' , 'blue' , 'orange' , 'red' , 'dark-blue']
colors.sort()   # Sort according to a-z in first letter in each word
print(colors)


print(marks.index(5))    # to find out the index number of "5" , which is 3
data = [5, 9, 5, 4, 3, 6, 7, 5, 9 , 6, 5, 6 , 5, 6, 6 , 6, 6, 5, 5, 5, 5, 8 , 5, 4, 6, 3, 8, 2, 6, 9, 2, 4, 3, 5, 1, 3]
print(data.count(5))    # Count how many 5 are there (11 times) with ,count() 


### New thing to learn
m = [3, 6, 4, 9, 6, 9, 5]
# l = m
# l[2] = 3    # Change the 2'index(3rd data) into '3'
print(m , "(original)")    # It may seems like only l has changed . But surprizingly m will also be changed

### So instead of copying a list into another by "=" , you had better use .copy() function .
l = m.copy()
l[2] = 3
print(m , "has been copied but not changed")    # In this way , you can copy "m" into "l" without changing "m"
print(l , ", New list has been created and changed")

l.insert(2, 7)    # Insert '7' in 2'index/3rd position
print(l , " Have been Inserted")