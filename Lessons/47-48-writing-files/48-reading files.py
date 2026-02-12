# Python reading files (.txt, .json, .csv)
import json
import csv

txt_path = "C:/Users/jan_n/Code/Neuer Ordner/Code/Lessons/47-48-writing-files/output.txt"
json_path = "C:/Users/jan_n/Code/Neuer Ordner/Code/Lessons/47-48-writing-files/output.json"
csv_path = "C:/Users/jan_n/Code/Neuer Ordner/Code/Lessons/47-48-writing-files/output.csv"

try:
    #---------.txt------------------
    # with open(txt_path, "r") as file:
    #     content = file.read()           
    #     print(content)
    #---------.json-----------------
    # with open(json_path, "r") as file:
    #     content = json.load(file)
    #     print(content["age"])         # can use a key to get a certain value
    #---------.csv------------------
    with open(csv_path, "r") as file:
        content = csv.reader(file)
        for line in content:            # for-loop needed to get the output. without for-loop, output given is a memory address
            print(line[0])              # can use an index to get a specified column
    

except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("You do not have permission to read that file")
except Exception:
    print("Something went wrong.")