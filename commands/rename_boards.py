import click
from rich.console import Console
from utils.storage import load_boards, save_boards

console = Console()

@click.command(name="rename-board")
@click.argument("old_name")
@click.argument("new_name")
def rename_board(old_name, new_name):

    """ rename an existing board """

    boards = load_boards()

    if old_name not in boards:

        console.print(f"[red]Board '{old_name}' does not exist.[/red]")
        return

    if new_name in boards:

        console.print(f"[red]Board '{new_name}' already exists. Choose a different name.[/red]")
        return

    boards[new_name] = boards.pop(old_name)
    save_boards(boards)
    console.print(f"[green]Board '{old_name}' renamed to '{new_name}'.[/green]")
