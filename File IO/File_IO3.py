###truncate(size) method is used to resize a file to a specified size. If the file is larger than the specified size, it will be truncated (shortened) to that size. If the file is smaller than the specified size, it remains unchanged.

with open('my_file5.txt' , 'w') as file:
    file.write("123456789ABCDEFGHIJKLMNOPQRSTUVWXYZfgoierknvfhuerbtnfjierbnfgoinher")
    file.truncate(35)    # To limit the text from 123... to ...XYZ and remove the remaining unnecessary letters



### ### ### ### ### ### seek(offset): ### ### ### ### ### ###
# The seek() method is used to change the current file position within a file.
# offset specifies the number of bytes to move the file pointer.
# After calling seek(), the file pointer is moved accordingly.
# While whence is used in write / 'w' mode

### ### ### ### ### ### tell(): ### ### ### ### ### ###
# The tell() method returns the current file position, i.e., the byte offset from the beginning of the file.
# It doesn't take any arguments.
# After calling tell(), it returns the current position as an integer.

with open('my_file5.txt' , 'r') as file:
    # Move the file pointer 5 bytes
    file.seek(5)
    print(file.tell())
    content = file.read()
    print(content)
    print(file.tell())