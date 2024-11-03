import json
import os

# file path for storing tasks
DATA_FILE = "data/tasks.json"
# makes sure data file and folder exist
os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
if not os.path.exists(DATA_FILE): # incase it doesn't exist
    with open(DATA_FILE, 'w') as f:
        json.dump({}, f) # create an empty list


def load_boards():

    """ Load all boards and their tasks. """

    try:

        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            # if data is an empty list reset to an empty dictionary
            if isinstance(data, list):
                data = {}
            return data
        
    except json.JSONDecodeError:
        return {}

def save_boards(boards):

    """ Save all boards and their tasks. """

    with open(DATA_FILE, 'w') as f:

        json.dump(boards, f, indent=4)

def load_board(board_name):

    """ Load tasks for a specific board. """

    boards = load_boards()
    return boards.get(board_name, [])

def add_board(board_name):

    """ Add a new board if it doesn't exist. """

    boards = load_boards()

    if board_name not in boards:

        boards[board_name] = []
        save_boards(boards)

def delete_board(board_name):

    """ Delete an existing board. """

    boards = load_boards()

    if board_name in boards:

        del boards[board_name]
        save_boards(boards)

def add_task_to_board(board_name, task):

    """ Add a task to a specific board. """

    boards = load_boards()

    if board_name in boards:

        boards[board_name].append(task)
        save_boards(boards)

def mark_task_done(board_name, task_id):

    """ Mark a task as done within a specific board. """

    boards = load_boards()

    if board_name in boards and 0 <= task_id < len(boards[board_name]):

        boards[board_name][task_id]["done"] = True
        save_boards(boards)

def delete_task_from_board(board_name, task_id):

    """ Delete a task from a specific board. """

    boards = load_boards()

    if board_name in boards and 0 <= task_id < len(boards[board_name]):
        
        del boards[board_name][task_id]
        save_boards(boards)