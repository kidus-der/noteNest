import click
from rich.console import Console
from utils.storage import unarchive_board

console = Console()

@click.command(name="unarchive-board")
@click.argument("board_name")
def unarchive_board_command(board_name):

    """Unarchive a board and move it back to active boards."""

    try:
        # call unarchive_board function from storage.py
        unarchive_board(board_name)
        console.print(f"[green]Board '{board_name}' has been successfully unarchived.[/green]")

    except ValueError as e:

        console.print(f"[red]{e}[/red]")
