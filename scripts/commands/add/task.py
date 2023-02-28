"""This module implements the tasks related to create a new todo item."""
from scripts.utils.constants import API_URL
from scripts.utils.request import Request


class Add():
    """Task to create a new todo item."""
    def __init__(self, text):
        self._text = text

    def run(self):
        """Run the task."""
        Request(API_URL, timeout=2.5).post(text=self._text)
