import click
from utils.storage import load_board, save_boards, get_task_note_path
from rich.console import Console

console = Console()

@click.command(name="add-note")
@click.argument("board_name")
@click.argument("task_id", type=int)
@click.option("--content", prompt="Enter your note", help="Content to add to the task note")
def add_note_to_task(board_name, task_id, content):

    """ add a note to a specific task within a board """
    tasks = load_board(board_name)

    if not tasks or task_id < 0 or task_id >= len(tasks):

        console.print(f"[red]Task #{task_id} does not exist in board '{board_name}'.[/red]")
        return

    # get the path to task's notes file
    note_path = get_task_note_path(board_name, task_id)

    # append the new content to the notes file
    with open(note_path, "a") as note_file:
        note_file.write(content + "\n")

    console.print(f"[green]Note added to task #{task_id} in board '{board_name}'.[/green]")
