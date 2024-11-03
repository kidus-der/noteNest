import click
from rich.console import Console
from rich.table import Table
from utils.storage import load_board

console = Console()

@click.command(name="list")
@click.argument("board_name")
@click.option("--sort-by", type=click.Choice(["priority", "due-date", "status"], case_sensitive=False), help="Sort tasks by priority, due-date, or status")
def list_tasks(board_name, sort_by):

    ''' lists all tasks created by user in a board, with optional sorting '''

    tasks = load_board(board_name)

    # check if tasks exist in board and output them in a table
    if not tasks:

        console.print(f"[yellow]No tasks found in board '{board_name}'.[/yellow]")
        return
    
    # sorting
    if sort_by == "priority":
        tasks.sort(key=lambda x: {"low": 1, "medium": 2, "high": 3}.get(x.get("priority", "low")))
    elif sort_by == "due-date":
        tasks.sort(key=lambda x: x.get("due_date", "9999-12-31"))  # default is far into the future(we go back when sorting time back to the future style)
    elif sort_by == "status":
        tasks.sort(key=lambda x: x["done"], reverse=True)  # completed tasks appear at the end


    # display sorted tasks
    table = Table(title=f"Tasks in '{board_name}'", show_header=True, header_style="bold magenta")
    table.add_column("ID #", style="dim", width=6)
    table.add_column("Description", min_width=30)
    table.add_column("Status", justify="center")
    table.add_column("Priority", justify="center")
    table.add_column("Due Date", justify="center")

    for i, task in enumerate(tasks):
        
        status = "[green]✔[/green]" if task["done"] else "[red]✘[/red]"
        table.add_row(str(i), task["description"], status, task["priority"], task["due_date"])

    console.print(table)