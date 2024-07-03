import webbrowser

print('He said, "I want to eat an apple".')
#OR
print("He said, \"I want to eat an apple\".")

receipe = """
1. Heat the pan and add oil
2. Crack the egg
3. Add salt in egg and mix well
4. Pour the mixture in pan
5. Fry on medium heat
"""
print(receipe)

note = '''
This is a multiline string
It is used to display multiline message in the program
'''
print(note)

fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")

for i in fruit:
    print(i)

pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index
#In case of negative index , consider it as : len(pie) - #(index)
#Example : [:-3] means starting to len(pie) - 3

a= 18
print("He is" , a , "years old")
print(type(a))


def open_webpage():
    url = 'https://www.codewithharry.com/tutorial/python-string-methods/'
    print("Click the link below to learn more about Sring  Method : ")
    print(url)

open_webpage()