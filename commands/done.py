import click
from rich.console import Console
from utils.storage import mark_task_done, load_board

console = Console()

@click.command()
@click.argument("board_name")
@click.argument("task_id", type=int)
def mark_done(board_name, task_id):

    ''' marks a task as done based on task_id '''

    tasks = load_board(board_name)

    # error handling for invalid task_id
    if not tasks or task_id < 0 or task_id >= len(tasks):

        console.print(f"[red]ERROR:[/red] Task #{task_id} does not exist in board '{board_name}'.")

    else:
                
        mark_task_done(board_name, task_id)
        console.print(f"[green]Task #{task_id} marked as done in board '{board_name}'.[/green]")