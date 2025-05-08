# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.



import os

# You can change this to any directory you want
directory_path = "/"

try:
    # List all files and directories in the specified path
    contents = os.listdir(directory_path)
    
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
