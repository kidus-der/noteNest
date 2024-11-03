import click
from rich.console import Console
from utils.storage import add_board, load_boards

console = Console()

@click.command()
@click.argument("board_name")
def create_board(board_name):

    ''' allows a user to 
    create a new board '''

    boards = load_boards()

    # check if board already exists or add one
    if board_name in boards:

        console.print(f"[yellow]Board '{board_name}' already exists.[/yellow]")

    else:

        add_board(board_name)
        console.print(f"[green]Board '{board_name}' created.[/green]")