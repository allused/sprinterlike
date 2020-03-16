import csv
import os
import random
import string

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def read_table_from_file(file_name, separator=';'):
    """Read CSV file into a data table.

    Args:
        file_name: The name of the CSV data file.
        separator: The CSV separator character

    Returns:
        The data parsed into a list of lists.
    """
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        return [element.replace("\n", "").split(separator) for element in lines]
    except IOError:
        return []

def write_table_to_file(file_name, table, separator=';'):
    """Write tabular data into a CSV file.

    Args:
        file_name: The name of the file to write to.
        table: list of lists containing tabular data.
        separator: The CSV separator character
    """
    with open(file_name, "w") as file:
        for record in table:
            row = separator.join(record)
            file.write(row + "\n")

def make_dict(data, headers):
    return [{headers[i]: stat for i, stat in enumerate(line)} for line in data]

def make_id(dicts):
    id = []
    id.append(random.choice(string.ascii_letters))
    id.append(random.choice(string.digits))
    for dict in dicts:
        if dict['id'] != id:
            return "".join(id)

def get_all_user_story():
    return []

def make_list(data):
    save_list = []
    for dict in data:
        current_list = []
        current_list.extend(dict.values())
        save_list.append(current_list)
    return save_list



data_list = read_table_from_file(DATA_FILE_PATH,';')
data_dict = make_dict(data_list, DATA_HEADER)
print(data_dict)