"""This module implements the commands to display a list of todo."""
import click
from click import ClickException
import logging

from scripts.utils.errors import TaskError
from .task import List


logger = logging.getLogger(__name__)


@click.command(name='list')
@click.option('-o', '--output', type=click.Choice(['table', 'txt', 'json'], case_sensitive=False), default='table',
              required=False, help="Output format. Default: table.")
def get_list(output):
    """List all todo items."""
    try:
        List(output).run()
    except TaskError as e:
        logger.error(f"{e.error_msg}. Additional info: {e.additional_info}")
        raise ClickException(f"An error occurred while listing the todo items. Additional info: {e.error_msg}") from e
