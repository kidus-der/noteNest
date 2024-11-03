import click
from rich.console import Console
from rich.table import Table
from utils.storage import load_board

console = Console()

@click.command(name="list")
@click.argument("board_name")
def list_tasks(board_name):

    ''' lists all tasks created by user in a board '''

    tasks = load_board(board_name)

    # check if tasks exist in board and output them in a table
    if not tasks:

        console.print(f"[yellow]No tasks found in board '{board_name}'.[/yellow]")

    else:

        # create a table to display tasks
        table = Table(title=f"Tasks in '{board_name}'", show_header=True, header_style="bold magenta")
        table.add_column("ID #", style="dim", width=6)
        table.add_column("Description", min_width=30)
        table.add_column("Status", justify="center")
        table.add_column("Priority", justify="center")
        table.add_column("Due Date", justify="center")

        for i, task in enumerate(tasks):
            
            status = "[green]✔[/green]" if task["done"] else "[red]✘[/red]"
            priority = task.get("priority", "N/A")
            due_date = task.get("due_date", "N/A")
            table.add_row(str(i), task["description"], status, priority, due_date)

        console.print(table)