import click
from rich.console import Console
from utils.storage import add_task_to_board, load_boards

console = Console()

@click.command(name="add")
@click.argument("board_name")
@click.argument("description")
def add_task(board_name, description):

    ''' allows user to add a task'''

    boards = load_boards()

    if board_name not in boards:
        console.print(f"[red]Board '{board_name}' does not exist. Create it first with 'create_board'.[/red]")
    else:
        task = {"description": description, "done": False}
        add_task_to_board(board_name, task)
        console.print(f"[green]Task added to '{board_name}':[/green] {description}")