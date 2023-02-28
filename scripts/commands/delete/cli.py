"""This module implements the commands to delete a todo item."""
import click
from click import ClickException
import logging

from scripts.utils.errors import TaskError
from .task import Delete


logger = logging.getLogger(__name__)


@click.command(name='delete')
@click.argument('text', type=str)
def delete_event(text):
    """Delete a todo item."""
    try:
        Delete(text).run()
    except TaskError as e:
        logger.error(f"{e.error_msg}. Additional info: {e.additional_info}")
        raise ClickException(f"An error occurred while deleting a todo item. Additional info: {e.error_msg}") from e
