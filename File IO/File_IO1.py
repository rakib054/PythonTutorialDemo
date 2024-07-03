### Reading File
try:
    file = open('my_file1.txt', 'r')    # Show Error if my_file.txt doesn't exist
    text = file.read()
    print(text)
    file.close()
except FileNotFoundError:
    print("Error: File not found")



### Writing File
file = open('my_file2.txt', 'w')    # If my_file2.txt doesn't exist , it create new one
file.write(text[:250])    # But it replace new content with previous one (by completely clearing it)
file.close()


### Appending File
with open('my_file3.txt', 'a') as file:
    file.write("Hey , I am Inside . Don't need to be surprized.\n")    # You don't need to close it