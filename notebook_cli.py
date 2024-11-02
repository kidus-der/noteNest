import click
from rich.console import Console
from rich.table import Table
import json
import os

# rich console object for styling output
console = Console()
# file path for storing tasks
DATA_FILE = "data/tasks.json"
# makes sure data file and folder exist
os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
if not os.path.exists(DATA_FILE): # incase it doesn't exist
    with open(DATA_FILE, 'w') as f:
        json.dump([], f) # create an empty list


def load_tasks():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)
    
def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# CLI commands group object
# didn't know click lets you create a group of subcommands
# under a group command (cli in this case)
@click.group()
def cli():
    "noteNest is a CLI notebook app for managing notes and tasks"
    pass

@cli.command()
@click.argument("description")
def add(description):
    ''' allows user to add a task'''

    tasks = load_tasks()
    task = {"description": description, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    console.print(f"[green]Task added:[/green] {description}") # rich stylized output :)

@cli.command()
def list():
    ''' lists all tasks created by user in a table'''

    tasks = load_tasks()
    if not tasks:
        console.print("[yellow]No tasks created yet :([/yellow]") # no tasks output
        return

    # rich table object for displaying tasks
    table = Table(title="Tasks", show_header=True, header_style="bold magenta")
    table.add_column("Done", style="dim", width=6)
    table.add_column("Description", min_width=20)
    table.add_column("Status", justify="center")

    # adding tasks to table based on:
    # task #, description, and completion status
    for i,task in enumerate (tasks):
        status = "[green]✔[/green]" if task["done"] else "[red]✘[/red]"
        table.add_row(str(i), task["description"], status)

    # output table
    console.print(table)