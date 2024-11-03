import click
from rich.console import Console
from rich.table import Table
from utils.storage import load_boards, load_board
from datetime import datetime

console = Console()

@click.command(name="search")
@click.option("--board", "board_name", type=str, help="Specify a board to search within")
@click.option("--description", type=str, help="Keyword to search in task descriptions")
@click.option("--status", type=click.Choice(["done", "not done"], case_sensitive=False), help="Filter by task completion status")
@click.option("--priority", type=click.Choice(["low", "medium", "high"], case_sensitive=False), help="Filter by task priority")
@click.option("--due-date", type=str, help="Filter by a specific due date (YYYY-MM-DD)")
def search_tasks(board_name, description, status, priority, due_date):

    """search for tasks across ALL boards based on filters,
    or within a user-specified board"""

    if board_name:
        # load tasks for the specified board only
        boards = {board_name: load_board(board_name)}

        if not boards[board_name]:  # check if board exists and is not empty
            console.print(f"[red]Board '{board_name}' does not exist or has no tasks :([/red]")
            return
    else:
        # load tasks for all boards
        boards = load_boards()
    
    results = []

    # check due date format
    if due_date:

        try:
            due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            console.print("[red]Invalid date format. Use YYYY-MM-DD.[/red]")
            return

    # filter tasks based on criteria
    for b_name, tasks in boards.items():

        for i, task in enumerate(tasks):

            match = True
            
            if description and description.lower() not in task["description"].lower():
                match = False
            if status:
                task_done = task["done"]
                if (status == "done" and not task_done) or (status == "not done" and task_done):
                    match = False
            if priority and task.get("priority") != priority:
                match = False
            if due_date and task.get("due_date") != due_date.strftime("%Y-%m-%d"):
                match = False
            
            # add task to results if all criteria match
            if match:
                results.append((b_name, i, task))

    # display results
    if not results:

        console.print("[yellow]No tasks found matching the criteria :([/yellow]")
        return

    table = Table(title="Search Results", show_header=True, header_style="bold magenta")
    table.add_column("Board", style="dim", width=12)
    table.add_column("ID #", style="dim", width=6)
    table.add_column("Description", min_width=30)
    table.add_column("Status", justify="center")
    table.add_column("Priority", justify="center")
    table.add_column("Due Date", justify="center")

    for b_name, task_id, task in results:

        status = "[green]✔[/green]" if task["done"] else "[red]✘[/red]"
        table.add_row(board_name, str(task_id), task["description"], status, task["priority"], task["due_date"])

    console.print(table)
