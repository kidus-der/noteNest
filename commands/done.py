import click
from rich.console import Console
from utils.storage import load_tasks, save_tasks

console = Console()

@click.command()
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