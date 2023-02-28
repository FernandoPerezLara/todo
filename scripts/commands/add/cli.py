"""This module implements the commands to create a new todo item."""
import logging
import click
from click import ClickException

from scripts.utils.errors import TaskError
from .task import Add


logger = logging.getLogger(__name__)


@click.command(name='add')
@click.argument('text', type=str)
def add_event(text):
    """Create a new todo item."""
    try:
        Add(text).run()
    except TaskError as e:
        logger.error(f"{e.error_msg}. Additional info: {e.additional_info}")
        raise ClickException(f"An error occurred while creating a new event. Additional info: {e.error_msg}") from e
