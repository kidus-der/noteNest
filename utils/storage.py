import json
import os

# file path for storing active boards
DATA_FILE = "data/active_boards.json"
# file path for archiving boards
ARCHIVE_FILE = "data/archive.json"
# Notes directory for storing task notes
NOTES_DIR = "notes/"

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

def load_archived_boards():

    """ Load archived boards. """

    if os.path.exists(ARCHIVE_FILE):
        try:
            with open(ARCHIVE_FILE, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    data = {}  
                return data
        except json.JSONDecodeError:
            return {}  # return an empty dict if the file is empty
    return {}

def save_archived_boards(boards):

    """ Save archived boards. """

    with open(ARCHIVE_FILE, 'w') as f:
        json.dump(boards, f, indent=4)

def archive_board(board_name):

    """ Move a board to the archive. """

    boards = load_boards()
    archived_boards = load_archived_boards()

    if board_name in boards:
        archived_boards[board_name] = boards.pop(board_name)
        save_boards(boards)
        save_archived_boards(archived_boards)

def initialize_notes_directory():

    """ Ensure the notes directory exists. """

    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)

def get_task_note_path(board_name, task_id):

    """ Get the file path for storing notes of a specific task. """
    
    board_dir = os.path.join(NOTES_DIR, board_name)
    os.makedirs(board_dir, exist_ok=True)
    return os.path.join(board_dir, f"task_{task_id}.txt")

def unarchive_board(board_name):

    """Move a board from the archive back to active boards."""

    archived_boards = load_archived_boards()
    active_boards = load_boards()

    if board_name in archived_boards:

        # move board data from archive to active boards
        active_boards[board_name] = archived_boards.pop(board_name)
        save_boards(active_boards)
        save_archived_boards(archived_boards)
        
    else:

        raise ValueError(f"Board '{board_name}' not found in archive.")