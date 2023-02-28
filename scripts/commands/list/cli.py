"""This module implements the commands to display a list of todo."""
import click

from .task import List


@click.command(name="list")
@click.option('-o', '--output', default='table', type=str, required=False,
              help="Output format. Options: txt, table, json. Default: table.")
def get_list(output):
    """List all todo items."""
    List(output).run()
