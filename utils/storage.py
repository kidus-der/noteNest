import json
import os

# file path for storing tasks
DATA_FILE = "data/tasks.json"
# makes sure data file and folder exist
os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
if not os.path.exists(DATA_FILE): # incase it doesn't exist
    with open(DATA_FILE, 'w') as f:
        json.dump([], f) # create an empty list


def load_tasks():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return [] # return an empty list if the file is empty or invalid
    
def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)