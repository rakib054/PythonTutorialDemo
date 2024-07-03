import os

### os.path.exists(path): Check whether a path exists
path = r"E:\Python Project\Tuple\02(More function).py"
exists = os.path.exists(path)
if exists:
    print("The path exists")
else:
    print("The path doesn't exists")


### os.path.isfile(path): Check whether a path is a regular file
file = r"E:\Python Project\Tuple\02(More function).py"
isfile = os.path.isfile(file)
if isfile:
    print("The file exists")
else:
    print("The file doesn't exists")


### os.path.isdir(path): Check whether a path is a directory
dir = r"E:\Python Project\Tuple"
isdir = os.path.isdir(dir)
if isdir:
    print("The directory(Not Path) exists")
else:
    print("The directory doesn't exists")


### os.path.splitext(path): Split the extension from a pathname:
#This function splits the extension from the specified pathname and returns a tuple containing the root and extension
path = r"E:\Python Project\Tuple\02(More function).py"
root, extention = os.path.splitext(path)
### os.path.basename(path): Return the base name of a pathname
basename = os.path.basename(path)
###os.path.dirname(path): Return the directory name of a pathname
dirname = os.path.dirname(path)


print(f"The Root of Path is : {root} of Path and the Extention is : {extention}")
print("The Base Name is : ", basename)
print("The Directory Name is : ", dirname)

