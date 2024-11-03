import click
from rich.console import Console
from utils.storage import load_boards

console = Console()

@click.command()
def list_boards():

    ''' lists all the boards a
    user has created '''

    boards = load_boards()

    
    if not boards:

        console.print("[yellow]No boards found, please create a board[/yellow]")

    else:

        console.print("[bold magenta]Boards:[/bold magenta]")
        for board in boards:
            
            console.print(f"- {board}")