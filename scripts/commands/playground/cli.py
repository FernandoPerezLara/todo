"""This module implements the commands to deploy the playground."""
import logging
import click
from click import ClickException

from .task import GenerateRandom, DeleteAll
from scripts.utils.errors import TaskError


logger = logging.getLogger(__name__)


@click.group()
def playground():
    """Parent command for playground operations."""


@playground.command(name='add')
def generate_random():
    """Create a random number of todo items between 10 and 100."""
    try:
        GenerateRandom().run()
    except TaskError as e:
        logger.error(f"{e.error_msg}. Additional info: {e.additional_info}")
        raise ClickException(f"An error occurred while creating a new event. Additional info: {e.error_msg}") from e


@playground.command(name='delete')
def delete_all():
    """Delete all the todo items."""
    try:
        DeleteAll().run()
    except TaskError as e:
        logger.error(f"{e.error_msg}. Additional info: {e.additional_info}")
        raise ClickException(f"An error occurred while deleting all the events. Additional info: {e.error_msg}") from e
