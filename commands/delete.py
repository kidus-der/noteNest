import click
from rich.console import Console
from utils.storage import delete_task_from_board, load_board

console = Console()

@click.command(name="delete")
@click.argument("board_name")
@click.argument("task_id", type=int)
def delete_task(board_name, task_id):

    ''' delete a task from the task list '''

    tasks = load_board(board_name)

    if not tasks or task_id < 0 or task_id >= len(tasks):

        console.print(f"[red]ERROR:[/red] Task #{task_id} does not exist in board '{board_name}'.")

    else:
        
        task_description = tasks[task_id]["description"]
        delete_task_from_board(board_name, task_id)
        console.print(f"[green]Task deleted from '{board_name}':[/green] {task_description}")