import click
from rich.console import Console
from utils.storage import load_tasks, save_tasks

console = Console()

@click.command(name="add")
@click.argument("description")
def add_task(description):
    ''' allows user to add a task'''

    tasks = load_tasks()
    task = {"description": description, "done": False}
    tasks.append(task) # add task to task list
    save_tasks(tasks)
    console.print(f"[green]Task added:[/green] {description}") # rich stylized output :)