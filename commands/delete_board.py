import click
from rich.console import Console
from utils.storage import delete_board, load_boards

console = Console()

@click.command(name="delete-board")
@click.argument("board_name")
def delete_board_command(board_name):

    """Delete an entire board and all its tasks."""

    boards = load_boards()

    if board_name not in boards:
        console.print(f"[red]Board '{board_name}' does not exist.[/red]")
        return

    # confirm with user
    confirm = input(f"Are you sure you want to delete the board '{board_name}' and all its tasks? (y/n): ")
    if confirm.lower() != 'y':
        console.print("[yellow]Board deletion canceled[/yellow]")
        return

    delete_board(board_name)
    console.print(f"[green]Board '{board_name}' deleted successfully[/green]")
