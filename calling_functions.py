from functions import categories, items_output, exist_items
import pathlib
from pathlib import Path

path = Path(pathlib.Path.cwd(), 'data', 'data.txt')
categories(path)

colour = 'black'
items_output(path, colour)

category_id = 1
exist_items(path, category_id)
