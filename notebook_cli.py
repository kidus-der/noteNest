import click
from rich.console import Console
from rich.table import Table
import json
import os

# rich console object for styling output
console = Console()
# file path for storing tasks
DATA_FILE = "data/tasks.json"
# makes sure data file and folder exist
os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
if not os.path.exists(DATA_FILE): # incase it doesn't exist
    with open(DATA_FILE, 'w') as f:
        json.dump([], f) # create an empty list


def load_tasks():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)
    
def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)
