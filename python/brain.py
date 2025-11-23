import csv
import json
import os

# function that reads a file and converts it into either csv or json.
def convert_from_file(file, to_csv=False, to_json=False):
    if to_json:
        with open(file, mode='r', newline='', encoding='utf-8') as csv_file:
            content = csv_file.read()
            return convert_from_text(content, to_json=True)

    elif to_csv:
        with open(file, mode='r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return convert_from_text(data, to_csv=True)


# if the input is text content rather than a file
def convert_from_text(content, to_json=False, to_csv=False):
    data = []
    text = read_text(content)
    # converts to json and returns the content of the created file
    if to_json:
        fieldnames = text[0].split(',')
        for line in text[1:]:
            values = line.split(',')
            entry = {field: value for field, value in zip(fieldnames, values)}
            data.append(entry)
        file = create_type_file(data, create_json_file=True)
        return json.loads(json.dumps(data, indent=4))
    # converts to csv and returns the content of the created
    elif to_csv:
        data = json.loads(content)
        file = create_type_file(data, create_csv_file=True)
        return file

    
# creates a file of the specified type
def create_type_file(data, create_json_file=False, create_csv_file=False):
    if create_json_file and data:
        
        # create a json file and returns the content of the file
        with open('python/results/output.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        return json.loads(json.dumps(data, indent=4))
    else:
        print("No data to write to JSON")

    if create_csv_file and data:
        
        # creates a csv file and returns the content of the file
        with open('python/results/output.csv', mode='w', newline='', encoding='utf-8') as csv_file:
            fieldnames = data[0].keys()
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(data)
            return csv_file.read()
    else:
        print("No data to write to CSV.")

# split lines when reading text in a csv format
def read_text(text):
    lines = text.splitlines()
    return lines