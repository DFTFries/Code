# Python file detection

#import os    # imports the operating system

# Relative file path = Lessons\46-file detection\test.txt
# Absolute file path = C:\Users\jan_n\Documents\code\Code\Lessons\46-file detection\test.txt

# file_path = "test.txt" #same folder only filename + extension needed

# if os.path.exists(file_path):
#     print(f"The location '{file_path}' exists")
# else:
#     print("That location doesn't exist")

import os

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesn't exist")