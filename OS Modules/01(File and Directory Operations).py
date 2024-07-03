import os

### os.getcwd(): Get the current working directory
cwd = os.getcwd()
print("Current working directory :", cwd, end="\n\n")

### os.listdir(path='.'): Return a list of the names of the files and directories in the specified directory
files = os.listdir(cwd)
print("Files and directories in the directory:")
for i in files:
    print(i)

### os.chdir(path): Change the current working directory to the specified path
os.chdir("E:\Python Project\List")
cwd = os.getcwd()    # To check if the directory has changed or not .....
print("Changed working directory:", cwd, end="\n\n")
files02 = os.listdir(cwd)
print(f"Files and directories in {cwd} is:")
for i in files02:
    print(i)




### ### ### ### os.mkdir() and os.makedirs() functions ### ### ### ###

### os.mkdir(path, mode=0o777, *, dir_fd=None): Create a directory with the specified path:This function creates a new directory with the specified path. It takes the following parameters:
# path: The path of the directory to be created.
# mode: The permissions to be set for the new directory. It's an optional parameter, and by default, it's set to 0o777, which means the directory will have full permissions (read, write, and execute) for the owner, group, and others.
# dir_fd: An optional file descriptor (integer) that specifies the directory where the new directory should be created. If provided, path should be relative to this directory.
# If the directory creation is successful, the function doesn't return anything. However, if an error occurs (e.g., if the directory already exists or the user doesn't have permission to create the directory), it raises an exception, typically FileExistsError.


### os.makedirs(name, mode=0o777, exist_ok=False): Recursively create directories:This function creates directories recursively, creating any missing parent directories as needed. It takes the following parameters:
# name: The path of the directory (or directories) to be created.
# mode: The permissions to be set for the new directories. Like os.mkdir(), it's an optional parameter, and by default, it's set to 0o777.
# exist_ok: If set to True, the function doesn't raise an exception if the directory already exists. If set to False (default), it raises FileExistsError if the directory already exists.
# If the directory creation is successful, the function doesn't return anything. If an error occurs during the creation of any directory, it raises an exception.
