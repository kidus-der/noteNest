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
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return [] # return an empty list if the file is empty or invalid
    
def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# CLI commands group object
# didn't know click lets you create a group of subcommands
# under a group command (cli in this case)
@click.group()
def cli():
    ''' noteNest is a CLI notebook app for managing notes and tasks '''
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

@cli.command()
@click.argument("task_id", type=int)
def done(task_id):
    ''' marks a task as done based on task_id '''

    tasks = load_tasks()

    # error handling for invalid task_id
    if task_id < 0 or task_id >= len(tasks):
        console.print(f"[red]ERROR:[/red] Task #{task_id} does not exist")
        return

    # marking task as done
    tasks[task_id]["done"] = True
    save_tasks(tasks)
    console.print(f"[green]Task marked as done:[/green] {tasks[task_id]['description']}")

@cli.command()
@click.argument("task_id", type=int)
def delete(task_id):
    ''' delete a task from the task list '''

    tasks = load_tasks()

    if task_id < 0 or task_id >= len(tasks):
        console.print(f"[red]ERROR:[/red] Task #{task_id} does not exist")
        return
    
    task_description = tasks[task_id]["description"]
    del tasks[task_id] # delete task
    save_tasks(tasks)
    console.print(f"[green]Task deleted:[/green] {task_description}")

if __name__ == "__main__":
    cli()