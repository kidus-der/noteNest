import click
from rich.console import Console
from utils.storage import archive_board, load_boards

console = Console()

@click.command(name="archive-board")
@click.argument("board_name")
def archive_board_command(board_name):

    """ archive a board and remove it from active boards"""

    boards = load_boards()

    if board_name not in boards:
        console.print(f"[red]Board '{board_name}' does not exist.[/red]")
        return

    archive_board(board_name)
    console.print(f"[green]Board '{board_name}' archived successfully.[/green]")
