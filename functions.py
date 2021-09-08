import json
import pathlib
from pathlib import Path

path = Path(pathlib.Path.cwd(), 'data', 'data.txt')
with open(path) as file:
    data = json.loads(file.read())


def categories(path):
    for i in data['categories']:
        print(i['name'])


colour = 'pink'


def items_output(path, colour):
    for i in data['items']:
        if i['color'] == colour:
            return print(i['name'])
    return print("The "+colour+" item was not found")


category_id = 1


def exist_items(path, category_id):
    for i in data['items']:
        if i['category_id'] == category_id:
            return print(True)
    return print(False)
