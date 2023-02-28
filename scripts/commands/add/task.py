"""This module implements the tasks related to create a new todo item."""
import logging

from scripts.utils.constants import API_URL
from scripts.utils.request import Request


logger = logging.getLogger(__name__)


class Add():
    """Task to create a new todo item."""
    def __init__(self, text):
        self._text = text

    def run(self):
        """Run the task."""
        logger.info(f"Adding todo item '{self._text}'.")
        Request(API_URL, timeout=2.5).post(text=self._text)
        logger.info(f"Todo item '{self._text}' added.")
