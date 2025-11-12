import csv
import json

# function that reads a file and converts it into either csv or json.
def convert_from_file(file, from_csv=False, from_json=False):
    if from_csv:
        with open(file, mode='r', newline='', encoding='utf-8') as csv_file:
            content = csv_file.read()
            convert_from_text(content, to_json=True)

    elif from_json:
        with open(file, mode='r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            create_type_file(data, create_csv_file=True)


# if the input is text content rather than a file
def convert_from_text(content, to_json=False, to_csv=False):
    data = []
    text = read_text(content)
    if to_json:
        fieldnames = text[0].split(',')
        for line in text[1:]:
            values = line.split(',')
            entry = {field: value for field, value in zip(fieldnames, values)}
            data.append(entry)
        create_type_file(data, create_json_file=True)
    elif to_csv:
        data = json.loads(content)
        create_type_file(data, create_csv_file=True)

    
    
def create_type_file(data, create_json_file=False, create_csv_file=False):
    if create_json_file:
        with open('output.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
    if create_csv_file:
        with open('output.csv', mode='w', newline='', encoding='utf-8') as csv_file:
            if data:
                fieldnames = data[0].keys()
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(data)

# split lines when reading text in a csv format
def read_text(text):
    lines = text.splitlines()
    return lines