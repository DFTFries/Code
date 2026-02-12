# Python writing files (.txt, .json, .csv)

txt_data = "I like pizza!"
employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]
employees_dict = {
    "name": "Spongebob",
    "age": 
}

file_path = "output.txt"
file2_path = "C:/Users/jan_n/Documents/test/output.txt"

# Modes:
# w = overwrite a file and create file if it doesn't exist
# x = write a file if it doesn't exist. if the file exists you get a FileExistsError
# a = append  - appends any new data to the file
# r = read

try:
    with open(file=file2_path, mode="w") as file:  
        for employee in employees:    
            file.write(employee + "\n")
        print(f"txt file {file2_path} was created.")
except FileExistsError:
    print("File already exists.")