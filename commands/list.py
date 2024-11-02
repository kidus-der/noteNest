import click
from rich.console import Console
from rich.table import Table
from utils.storage import load_tasks

console = Console()

@click.command(name="list")
def list_tasks():
    ''' lists all tasks created by user in a table '''

    tasks = load_tasks()
    if not tasks:
        console.print("[yellow]No tasks created yet :([/yellow]") # no tasks output
        return

    # rich table object for displaying tasks
    table = Table(title="Tasks", show_header=True, header_style="bold magenta")
    table.add_column("ID #", style="dim", width=6)
    table.add_column("Description", min_width=30)
    table.add_column("Status", justify="center")

    # adding tasks to table based on:
    # task #, description, and completion status
    for i,task in enumerate (tasks):
        status = "[green]✔[/green]" if task["done"] else "[red]✘[/red]"
        table.add_row(str(i), task["description"], status)

    # output table
    console.print(table)