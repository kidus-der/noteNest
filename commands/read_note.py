import os
import click
from utils.storage import load_board, get_task_note_path
from rich.console import Console

console = Console()

@click.command(name="read-note")
@click.argument("board_name")
@click.argument("task_id", type=int)
def read_note_from_task(board_name, task_id):

    """ read the notes for a specific task within a board """

    tasks = load_board(board_name)

    if not tasks or task_id < 0 or task_id >= len(tasks):

        console.print(f"[red]Task #{task_id} does not exist in board '{board_name}'.[/red]")
        return

    # get path for task's notes file
    note_path = get_task_note_path(board_name, task_id)

    # check if file exists and read contents
    if not os.path.exists(note_path):
        
        console.print(f"[yellow]No notes found for task #{task_id} in board '{board_name}'.[/yellow]")
        return

    with open(note_path, "r") as note_file:
        notes = note_file.read()

    console.print(f"[bold cyan]Notes for Task #{task_id} in '{board_name}':[/bold cyan]")
    console.print(notes if notes else "[yellow]No content in notes.[/yellow]")
