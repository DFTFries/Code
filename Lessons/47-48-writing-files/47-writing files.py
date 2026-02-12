# Python writing files (.txt, .json, .csv)

import json
import csv


txt_data = "I like pizza!"
employees_txt = ["Eugene", "Squidward", "Spongebob", "Patrick", "Larry"]

employees_json = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook",
}

employees_csv = [["Name", "Age", "Job"],
                 ["Spongebob", 30, "Cook"],
                 ["Patrick", 37, "Unemployed"],
                 ["Sandy", 27, "Scientist"]]

dir = "Lessons\\47-48-writing-files\\"
txt_path = dir + "output.txt"
json_path = dir + "output.json"
csv_path = dir + "output.csv"


# Modes:
# w = overwrite a file and create file if it doesn't exist
# x = write a file if it doesn't exist. if the file exists you get a FileExistsError
# a = append  - appends any new data to the file
# r = read

try:
    # with open(file=txt_path, mode="w") as file:  
    #     for employee in employees_txt:    
    #         file.write(employee + "\n")
    #     print(f"txt file {txt_path} was created.")

    # with open(json_path, "w") as file:
    #     json.dump(employees_json, file, indent=4)       #.dump() converts dictionary into json string
    #     print(f"json file '{json_path}' was created")

    with open(csv_path, "x", newline="") as file:
        writer = csv.writer(file)
        for row in employees_csv:
            writer.writerow(row)
        print(f"csv file '{csv_path}' was created.")

except FileExistsError:
    print("File already exists.")

