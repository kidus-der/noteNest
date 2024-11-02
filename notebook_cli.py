import click
from commands.add import add_task
from commands.list import list_tasks
from commands.done import done
from commands.delete import delete_task

# CLI commands group object
# didn't know click lets you create a group of subcommands
# under a group command (cli in this case)
@click.group()
def cli():
    ''' noteNest is a CLI notebook app for managing notes and tasks '''
    pass

# register CLI commands
cli.add_command(add_task, name="add")
cli.add_command(list_tasks, name="list")
cli.add_command(done)
cli.add_command(delete_task, name="delete")

if __name__ == "__main__":
    cli()