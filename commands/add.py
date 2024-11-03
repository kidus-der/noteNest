import click
from rich.console import Console
from utils.storage import add_task_to_board, load_boards
from datetime import datetime

console = Console()

@click.command(name="add")
@click.argument("board_name")
@click.argument("description")
@click.option("--priority", type=click.Choice(["low", "medium", "high"], case_sensitive=False), default="low", help="Priority level of the task")
@click.option("--due-date", type=str, help="Due date for the task (YYYY-MM-DD)")
def add_task(board_name, description, priority, due_date):

    ''' allows user to add a task to a specified
    board with priority level and due dates'''

    boards = load_boards()

    if board_name not in boards:
        console.print(f"[red]Board '{board_name}' does not exist. Create it first with 'create_board'.[/red]")
        return
    
    # validate due date format (YYYY-MM-DD)
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            console.print("[red]Invalid date format. Use YYYY-MM-DD.[/red]")
            return
    
    # create the task object
    task = {
        "description": description,
        "done": False,
        "priority": priority,
        "due_date": due_date or "N/A"  # default to "N/A" if no due date is added
    }
    
    add_task_to_board(board_name, task)
    console.print(f"[green]Task added to '{board_name}' with priority '{priority}' and due date '{due_date or 'N/A'}'.[/green]")