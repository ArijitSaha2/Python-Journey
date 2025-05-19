# Label the program written in problem4.py with comments.

import os
# Select the directory path whose content you want to be listed
directory_path = "."
try:
    # Lists all the files and directories of the specified path
    contents = os.listdir(directory_path)
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")



































import os # Imports OS module

directory_path = "."  # Select the directory whose contents you want to be listed

try:
    contents = os.listdir(directory_path) # Lists all the files, paths and directories of the specified path
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")