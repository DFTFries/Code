# Python file detection

import os    # imports the operating system

# Relative file path = stuff/test.txt
# Absolute file path = C:/Users/jan_n/Documents/code/Code/Lessons/46-file detection/stuff/test.txt

file_path = "stuff/test.txt" # if same folder only filename + extension needed
file2_path = "C:\\Users\\jan_n\\Documents\\test\\test.txt" # use double backslash \\ or /
folder_path = "C:/Users/jan_n/Documents/test"

if os.path.exists(folder_path):
    print(f"The location '{folder_path}' exists")

    if os.path.isfile(folder_path):
        print("That is a file.")
    elif os.path.isdir(folder_path):
        print("That is a directory.")
else:
    print("That location doesn't exist")

