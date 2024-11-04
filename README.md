# noteNest

noteNest is a CLI notebook app designed to help users organize tasks within boards and keep detailed notes within each task. It offers flexibility for personal project management, task prioritization, and detailed note-taking, making it ideal for users who prefer a command-line environment for staying organized.

## Features

1) Board Management:

    - Create boards to group related tasks.
    - List existing boards.
    - Rename or archive boards for easy organization.

2) Task Management:

    - Add tasks to specific boards.
    - List tasks within a board with optional sorting by priority, due date, or status.
    - Mark tasks as done or delete tasks within a board.
    - Filter tasks by description, status, priority, and due date.

3) Note-taking within Tasks:

    - Open a task as a “file” to add notes.
    - Save and read notes within tasks for future reference.


## Technologies Used

- Python: Primary programming language.
- Click Python Library: For building the command-line interface.
- Rich Python Library: For enhanced output formatting in the terminal.
- JSON: For storing board, task, and note data in active_boards.json and archive.json.


## Installation
- Stuff here



## How to Use noteNest:

### Running the CLI App

- Use the following command to launch noteNest:
```python3 notenest_cli.py```

### Commands Overview

#### I) Board Management

##### Creating a Board

```python3 notenest_cli.py create-board <board_name>```

- Creates a new board with the given name.

##### Listing all Boards

```python3 notenest_cli.py list-boards```

- Displays a list of all created boards.

##### Renaming a Board

```python3 notenest_cli.py rename-board <old_name> <new_name>```

- Renames an existing board to a new name.

##### Archiving a Board

```python3 notenest_cli.py archive-board <board_name>```

- Moves the specified board and its tasks to the archive.

#### II) Task Management

##### Add a Task to Board

```python3 notenest_cli.py add <board_name> <description> [--priority <priority>] [--due-date <YYYY-MM-DD>]```

- Adds a task to the specified board with optional priority (low, medium, high) and due date.

##### List Tasks in a Board

```python3 notenest_cli.py list <board_name> [--sort-by priority|due-date|status]```

- Lists tasks within a board, with options to sort by priority, due date, or completion status.

##### Mark a Task as Done

```python3 notenest_cli.py done <board_name> <task_id>```

- Marks the specified task as done within a board.

##### Delete a Task

```python3 notenest_cli.py delete <board_name> <task_id>```

- Deletes a task from a specified board.

##### Search Tasks (either in all Boards or in specific Board with option command)

```python3 notenest_cli.py search [--board <board_name>] [--description <keyword>] [--status <done|not done>] [--priority <priority>] [--due-date <YYYY-MM-DD>]```

- Searches for tasks based on filters such as board name, keywords in the description, status, priority, and due date.

#### III) Note Management

##### Add a Note to a Task

```python3 notenest_cli.py add-note <board_name> <task_id> --content "<note_content>"```

- Opens the specified task as a “file” and appends notes to it.

##### Read Notes from a Task:

```python3 notenest_cli.py read-note <board_name> <task_id>```

- Displays the saved notes for a specified task.

## Data Storage

- data/active_boards.json: Stores active boards and their tasks.

- data/archive.json: Stores archived boards and their tasks.

- notes/ Directory: Each board has a subdirectory where task-specific note files are stored.
  - For example, notes/personal/task_0.txt contains notes for task #0 within the personal board.

## Future Features

Some future features to expand noteNest’s functionality include:

- Recurring Tasks: Support for recurring tasks that automatically reappear based on a specified schedule.

- Task Dependencies: Dependencies between tasks to enforce specific order of completion.

- Reminders: Notification system for tasks nearing their due date.

- Team Collaboration: Support for multi-user access and shared boards.
