import click
from rich.console import Console
from utils.storage import load_tasks, save_tasks

console = Console()

@click.command(name="delete")
@click.argument("task_id", type=int)
def delete_task(task_id):
    ''' delete a task from the task list '''

    tasks = load_tasks()

    if task_id < 0 or task_id >= len(tasks):
        console.print(f"[red]ERROR:[/red] Task #{task_id} does not exist")
        return
    
    task_description = tasks[task_id]["description"]
    del tasks[task_id] # delete task
    save_tasks(tasks)
    console.print(f"[green]Task deleted:[/green] {task_description}")