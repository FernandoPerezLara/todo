"""This module implements the commands to display a list of todo."""
import click

from scripts.utils.errors import TaskError
from .task import List


@click.command(name="list")
@click.option('-o', '--output', default='table', type=str, required=False,
              help="Output format. Options: txt, table, json. Default: table.")
def get_list(output):
    """List all todo items."""
    try:
        List(output).run()
    except TaskError as e:
        raise TaskError(f"An error occurred while listing the todo items. Additional info: {e.additional_info}") from e
